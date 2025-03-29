import { useEffect, useState } from 'react';
import { getCultureIdioms, IdiomItem } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';

interface IdiomsGameProps {
  enemyScore: number;
  onWin: () => void;
  onLose: () => void;
  timeLimit?: number; // Time limit in seconds (default: 120)
}

function IdiomsGame({ enemyScore, onWin, onLose, timeLimit = 120 }: IdiomsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [idiomItem, setIdiomItem] = useState<IdiomItem | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [selectedExpressionIndex, setSelectedExpressionIndex] = useState<number | null>(null);
  const [gameOver, setGameOver] = useState(false);
  const [correct, setCorrect] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [currentRound, setCurrentRound] = useState(1);
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);

  const fetchNewIdiom = async () => {
    try {
      setLoading(true);
      setSelectedExpressionIndex(null);
      setGameOver(false);
      setCorrect(false);
      
      const data = await getCultureIdioms();
      setIdiomItem(data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load game data');
      setLoading(false);
      console.error(err);
    }
  };

  useEffect(() => {
    fetchNewIdiom();
  }, []);

  const startNewGame = () => {
    setCurrentRound(1);
    setCurrentScore(0);
    fetchNewIdiom();
  };

  const handleExpressionSelect = (index: number) => {
    if (gameOver || selectedExpressionIndex !== null) return;
    
    setSelectedExpressionIndex(index);
    
    if (idiomItem && index === idiomItem.fake_index) {
      setCorrect(true);
      // Score based on difficulty level
      let difficultyScore;
      if (idiomItem.difficulty === 1) {
        difficultyScore = 200;
      } else if (idiomItem.difficulty === 2) {
        difficultyScore = 300;
      } else {
        difficultyScore = 500;
      }
      const newScore = currentScore + difficultyScore;
      setCurrentScore(newScore);
      setGameOver(true);
      
      // Vérifier si le score actuel dépasse le score ennemi
      if (newScore > enemyScore) {
        setTimeout(() => {
          setShowWinAnimation(true);
        }, 1500);
      } else {
        // Continuer le jeu avec un nouvel idiome
        setTimeout(() => {
          setCurrentRound(prev => prev + 1);
          fetchNewIdiom();
        }, 1500);
      }
    } else {
      setCorrect(false);
      const newScore = Math.max(0, currentScore - 100);
      setCurrentScore(newScore);
      setGameOver(true);
      
      // Si la réponse est incorrecte, continuer avec un nouvel idiome
      // à moins que le score soit suffisant pour gagner
      if (newScore > enemyScore) {
        setTimeout(() => {
          setShowWinAnimation(true);
        }, 1500);
      } else {
        setTimeout(() => {
          setCurrentRound(prev => prev + 1);
          fetchNewIdiom();
        }, 2000);
      }
    }
  };

  const handleTimeUp = () => {
    // Vérifier si le score est suffisant pour gagner
    if (currentScore > enemyScore) {
      setShowWinAnimation(true);
    } else {
      setShowLoseOverlay(true);
    }
  };

  const handleNextRound = () => {
    setShowWinAnimation(false);
    onWin();
  };

  const handleReturnToMenu = () => {
    setShowLoseOverlay(false);
    onLose();
  };

  if (loading && !idiomItem) {
    return <div className="culture-game-container">Loading game data...</div>;
  }

  if (error) {
    return <div className="culture-game-container">Error: {error}</div>;
  }

  return (
    <div className="culture-game-container">
      {showWinAnimation && <WinAnimation onNextRound={handleNextRound} />}
      {showLoseOverlay && <LoseOverlay onReturnToMenu={handleReturnToMenu} />}
      <Timer 
        duration={timeLimit} 
        initialTime={timeRemaining}
        onTimeUp={handleTimeUp}
        onTimeChange={setTimeRemaining}
      />
      
      <div className="score-display">
        Score: {currentScore} / Enemy Score: {enemyScore}
      </div>
      
      <div className="instructions">
        <h3>Find the Non-Existent Idiom!</h3>
        <p>One of these expressions is not a real English idiom. Can you spot the fake one?</p>
        <p className="round-counter">Round {currentRound}</p>
      </div>
      
      {idiomItem && (
        <div className="idioms-game">
          {idiomItem.expressions.map((expression, index) => (
            <div 
              key={index}
              className={`idiom-card ${
                selectedExpressionIndex === index 
                  ? (index === idiomItem.fake_index ? 'correct' : 'incorrect') 
                  : ''
              } ${gameOver && index === idiomItem.fake_index && selectedExpressionIndex !== index ? 'highlight' : ''}`}
              onClick={() => handleExpressionSelect(index)}
            >
              <p className="idiom-text">"{expression}"</p>
              
              {selectedExpressionIndex === index && (
                <div className="result-indicator">
                  {index === idiomItem.fake_index ? '✓' : '✗'}
                </div>
              )}
            </div>
          ))}
          
          {gameOver && (
            <div className="explanation-box">
              <p>{idiomItem.explanation}</p>
              {currentScore <= enemyScore && <p className="next-round-hint">Next round in a moment...</p>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default IdiomsGame;
