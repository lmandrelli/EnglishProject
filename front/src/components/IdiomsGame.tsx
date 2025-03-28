import { useEffect, useState } from 'react';
import { getCultureIdioms, IdiomItem } from '../services/gameService';
import './CultureGames.css';

interface IdiomsGameProps {
  enemyScore: number;
  onWin: () => void;
  onLose: () => void;
}

function IdiomsGame({ enemyScore, onWin, onLose }: IdiomsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [idiomItem, setIdiomItem] = useState<IdiomItem | null>(null);
  const [selectedExpressionIndex, setSelectedExpressionIndex] = useState<number | null>(null);
  const [gameOver, setGameOver] = useState(false);
  const [correct, setCorrect] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [currentRound, setCurrentRound] = useState(1);
  const [maxRounds] = useState(3);

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

  const handleExpressionSelect = (index: number) => {
    if (gameOver || selectedExpressionIndex !== null) return;
    
    setSelectedExpressionIndex(index);
    
    if (idiomItem && index === idiomItem.fake_index) {
      setCorrect(true);
      setCurrentScore(prev => prev + 300);
      setGameOver(true);
      
      if (currentRound >= maxRounds) {
        if (currentScore + 300 > enemyScore) {
          setTimeout(() => onWin(), 1500);
        } else {
          setTimeout(() => onLose(), 1500);
        }
      } else {
        setTimeout(() => {
          setCurrentRound(prev => prev + 1);
          fetchNewIdiom();
        }, 1500);
      }
    } else {
      setCorrect(false);
      setCurrentScore(prev => Math.max(0, prev - 100));
      setGameOver(true);
      
      if (currentRound >= maxRounds) {
        setTimeout(() => onLose(), 1500);
      } else {
        setTimeout(() => {
          setCurrentRound(prev => prev + 1);
          fetchNewIdiom();
        }, 1500);
      }
    }
  };

  if (loading && !idiomItem) {
    return <div className="culture-game-container">Loading game data...</div>;
  }

  if (error) {
    return <div className="culture-game-container">Error: {error}</div>;
  }

  return (
    <div className="culture-game-container">
      <div className="score-display">
        Score: {currentScore} / Enemy Score: {enemyScore}
      </div>
      
      <div className="instructions">
        <h3>Find the Non-Existent Idiom!</h3>
        <p>One of these expressions is not a real English idiom. Can you spot the fake one?</p>
        <p className="round-counter">Round {currentRound} of {maxRounds}</p>
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
              {currentRound < maxRounds && <p className="next-round-hint">Next round in a moment...</p>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default IdiomsGame;