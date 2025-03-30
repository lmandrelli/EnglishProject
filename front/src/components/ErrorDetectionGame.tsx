import { useEffect, useState } from 'react';
import { getGrammarOddOneOut, OddOneOutItem } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';

interface ErrorDetectionGameProps {
  enemyScore: number;
  onWin: (score: number) => void;
  onLose: (score: number) => void;
  timeLimit?: number; // Time limit in seconds (default: 120)
  currentScore?: number;
}

function ErrorDetectionGame({ enemyScore, onWin, onLose, timeLimit = 120 }: ErrorDetectionGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [grammarItem, setGrammarItem] = useState<OddOneOutItem | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [selectedSentenceIndex, setSelectedSentenceIndex] = useState<number | null>(null);
  const [gameOver, setGameOver] = useState(false);
  const [correct, setCorrect] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [currentRound, setCurrentRound] = useState(1);
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);

  const fetchNewSentence = async () => {
    try {
      setLoading(true);
      setSelectedSentenceIndex(null);
      setGameOver(false);
      setCorrect(false);
      
      const data = await getGrammarOddOneOut();
      setGrammarItem(data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load game data');
      setLoading(false);
      console.error(err);
    }
  };

  useEffect(() => {
    fetchNewSentence();
  }, []);

  const startNewGame = () => {
    setCurrentRound(1);
    setCurrentScore(0);
    fetchNewSentence();
  };

  const handleSentenceSelect = (index: number) => {
    if (gameOver || selectedSentenceIndex !== null) return;
    
    setSelectedSentenceIndex(index);
    
    if (grammarItem && index === grammarItem.correct_index) {
      setCorrect(true);
      // Score based on difficulty level
      let difficultyScore;
      if (grammarItem.difficulty === 1) {
        difficultyScore = 200;
      } else if (grammarItem.difficulty === 2) {
        difficultyScore = 300;
      } else {
        difficultyScore = 500;
      }
      const newScore = currentScore + difficultyScore;
      setCurrentScore(newScore);
      setGameOver(true);
      
      if (newScore > enemyScore) {
        setTimeout(() => {
          setShowWinAnimation(true);
        }, 1500);
      } else {
        setTimeout(() => {
          setCurrentRound(prev => prev + 1);
          fetchNewSentence();
        }, 1500);
      }
    } else {
      setCorrect(false);
      const newScore = Math.max(0, currentScore - 100);
      setCurrentScore(newScore);
      setGameOver(true);
      
      if (newScore > enemyScore) {
        setTimeout(() => {
          setShowWinAnimation(true);
        }, 1500);
      } else {
        setTimeout(() => {
          setCurrentRound(prev => prev + 1);
          fetchNewSentence();
        }, 2000);
      }
    }
  };

  const handleTimeUp = () => {
    if (currentScore > enemyScore) {
      setShowWinAnimation(true);
    } else {
      setShowLoseOverlay(true);
    }
  };

  const handleNextRound = () => {
    setShowWinAnimation(false);
    onWin(currentScore);
  };

  const handleReturnToMenu = () => {
    setShowLoseOverlay(false);
    onLose(currentScore);
  };

  if (loading && !grammarItem) {
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
        <h3>Find the Incorrect Sentence!</h3>
        <p>One of these sentences contains a grammatical error. Can you find it?</p>
        <p className="round-counter">Round {currentRound}</p>
      </div>
      
      {grammarItem && (
        <div className="idioms-game">
          {grammarItem.words.map((sentence, index) => (
            <div 
              key={index}
              className={`idiom-card ${
                selectedSentenceIndex === index 
                  ? (index === grammarItem.correct_index ? 'correct' : 'incorrect') 
                  : ''
              } ${gameOver && index === grammarItem.correct_index && selectedSentenceIndex !== index ? 'highlight' : ''}`}
              onClick={() => handleSentenceSelect(index)}
            >
              <p className="idiom-text">"{sentence}"</p>
              
              {selectedSentenceIndex === index && (
                <div className="result-indicator">
                  {index === grammarItem.correct_index ? '✓' : '✗'}
                </div>
              )}
            </div>
          ))}
          
          {gameOver && (
            <div className="explanation-box">
              <p>{grammarItem.explanation}</p>
              {currentScore <= enemyScore && <p className="next-round-hint">Next round in a moment...</p>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default ErrorDetectionGame;
