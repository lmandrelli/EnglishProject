import { useState, useEffect } from 'react';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import { getGrammarVerbConjugation, VerbConjugationItem } from '../services/gameService';
import './VerbFormsGame.css';

type VerbFormItem = VerbConjugationItem;

interface VerbFormsGameProps {
  enemyScore: number;
  onWin: (score: number) => void;
  onLose: (score: number) => void;
  timeLimit?: number;
  currentScore?: number;
}

function VerbFormsGame({ enemyScore, onWin, onLose, timeLimit = 120 }: VerbFormsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [gameData, setGameData] = useState<VerbFormItem | null>(null);
  const [userInput, setUserInput] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [hasWon, setHasWon] = useState(false);

  const fetchData = async () => {
    try {
      setLoading(true);
      const data = await getGrammarVerbConjugation();
      setGameData(data);
      setUserInput('');
      setIsCorrect(null);
      setLoading(false);
    } catch (err) {
      setError('Failed to load game data');
      setLoading(false);
      console.error(err);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value.toLowerCase();
    setUserInput(value);
    
    if (gameData && value === gameData.correct_form.toLowerCase()) {
      handleCorrectAnswer();
    }
  };

  const handleVictory = () => {
    if (!hasWon) {
      setHasWon(true);
      setShowWinAnimation(true);
    }
  };
  
  const handleCorrectAnswer = () => {
    if (gameData) {
      setIsCorrect(true);
      const points = gameData.difficulty === 1 ? 100 : gameData.difficulty === 2 ? 150 : 300;
      const newScore = currentScore + points;
      setCurrentScore(newScore);

      if (newScore > enemyScore) {
        setTimeout(handleVictory, 500);
      } else {
        setTimeout(() => {
          fetchData();
        }, 1000);
      }
    }
  };

  const handleTimeUp = () => {
    if (!hasWon && currentScore > enemyScore) {
      handleVictory();
    } else if (!hasWon) {
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

  if (loading) {
    return <div className="verb-forms-container">Loading game data...</div>;
  }

  if (error) {
    return <div className="verb-forms-container">Error: {error}</div>;
  }

  if (!gameData) {
    return <div className="verb-forms-container">No game data available</div>;
  }

  const renderSentence = () => {
    const parts = gameData.sentence.split(/{verb}/);
    return (
      <>
        {parts[0]}
        <span className={`verb-input-container ${isCorrect === true ? 'correct' : isCorrect === false ? 'incorrect' : ''}`}>
          <input
            type="text"
            value={userInput}
            onChange={handleInputChange}
            placeholder={gameData.verb}
            className="verb-input"
            autoFocus
          />
        </span>
        {parts[1]}
      </>
    );
  };

  return (
    <div className="verb-forms-container">
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
        <h3>Conjugate the verb correctly!</h3>
        <p>Use the given verb and tense to complete the sentence.</p>
      </div>

      <div className="verb-forms-game">
        <div className="game-info">
          <div className="verb-info">
            <span className="info-label">Verb:</span>
            <span className="info-value">{gameData.verb}</span>
          </div>
          <div className="tense-info">
            <span className="info-label">Tense:</span>
            <span className="info-value">{gameData.tense}</span>
          </div>
        </div>

        <div className="sentence-section">
          {renderSentence()}
        </div>
      </div>
    </div>
  );
}

export default VerbFormsGame;
