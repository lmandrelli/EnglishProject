import { useState, useEffect } from 'react';
import { getVocabularyGapFill, GapFillItem } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';


interface WordCompletionGameProps {
  enemyScore: number;
  onWin: () => void;
  onLose: () => void;
  timeLimit?: number;
}

function WordCompletionGame({ enemyScore, onWin, onLose, timeLimit = 120 }: WordCompletionGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [gameData, setGameData] = useState<GapFillItem | null>(null);
  const [shuffledWords, setShuffledWords] = useState<string[]>([]);
  const [selectedGap, setSelectedGap] = useState<number | null>(null);
  const [completedGaps, setCompletedGaps] = useState<{ [key: number]: string }>({}); 
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);

  const fetchData = async () => {
    try {
      setLoading(true);
      const data = await getVocabularyGapFill();
      const shuffled = [...data.words].sort(() => Math.random() - 0.5);
      setGameData(data);
      setShuffledWords(shuffled);
      setSelectedGap(null);
      setCompletedGaps({});
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

  const handleGapSelect = (index: number) => {
    if (!completedGaps[index]) {
      setSelectedGap(index);
    }
  };

  const handleWordSelect = (word: string, index: number) => {
    if (selectedGap !== null) {
      if (gameData && word === gameData.words[selectedGap]) {
        const newCompletedGaps = { ...completedGaps, [selectedGap]: word };
        setCompletedGaps(newCompletedGaps);

        // Calculate score based on difficulty
        const points = gameData.difficulty === 1 ? 100 : gameData.difficulty === 2 ? 150 : 300;
        const newScore = currentScore + points;
        setCurrentScore(newScore);

        // Check if all gaps are filled
        if (Object.keys(newCompletedGaps).length === gameData.words.length) {
          if (newScore > enemyScore) {
            setTimeout(() => {
              setShowWinAnimation(true);
            }, 500);
          } else {
            fetchData();
          }
        }
      } else {
        // Wrong match
        setCurrentScore(prevScore => Math.max(0, prevScore - 50));
      }
      setSelectedGap(null);
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
    onWin();
  };

  const handleReturnToMenu = () => {
    setShowLoseOverlay(false);
    onLose();
  };

  if (loading) {
    return <div className="culture-game-container">Loading game data...</div>;
  }

  if (error) {
    return <div className="culture-game-container">Error: {error}</div>;
  }

  if (!gameData) {
    return <div className="culture-game-container">No game data available</div>;
  }

  const renderText = () => {
    const parts = gameData.text.split(/(\{[0-9]+\})/);
    return parts.map((part, index) => {
      const gapMatch = part.match(/\{([0-9]+)\}/);
      if (gapMatch) {
        const gapNumber = parseInt(gapMatch[1]) - 1;
        return (
          <span 
            key={index}
            className={`gap ${selectedGap === gapNumber ? 'selected' : ''} ${completedGaps[gapNumber] ? 'completed' : ''}`}
            onClick={() => handleGapSelect(gapNumber)}
          >
            {completedGaps[gapNumber] || '_____'}
          </span>
        );
      }
      return <span key={index}>{part}</span>;
    });
  };

  return (
    <div className="culture-game-container">
      {showWinAnimation && <WinAnimation onNextRound={handleNextRound} />}
      {showLoseOverlay && <LoseOverlay onReturnToMenu={handleReturnToMenu} />}
      <Timer 
        duration={timeLimit}
        onTimeUp={handleTimeUp}
      />
      
      <div className="score-display">
        Score: {currentScore} / Enemy Score: {enemyScore}
      </div>
      
      <div className="instructions">
        <h3>Complete the text with the correct words!</h3>
        <p>Click on a gap to see its definition, then select the matching word.</p>
      </div>

      <div className="word-completion-game">
        <div className="text-section">
          {renderText()}
        </div>

        <div className="info-section">
          {selectedGap !== null && (
            <div className="definition-box">
              <h4>Definition:</h4>
              <p>{gameData.definitions[selectedGap]}</p>
            </div>
          )}

          <div className="words-grid">
            {shuffledWords.map((word, index) => (
              <div
                key={`${word}-${index}`}
                className={`word-card ${Object.values(completedGaps).includes(word) ? 'matched' : ''}`}
                onClick={() => !Object.values(completedGaps).includes(word) && handleWordSelect(word, index)}
              >
                {word}
              </div>
            ))}
          </div>
        </div>
      </div>

      <style>{`
        .word-completion-game {
          display: flex;
          flex-direction: column;
          gap: 2rem;
          padding: 1rem;
        }

        .text-section {
          background: rgba(0, 0, 0, 0.2);
          padding: 2rem;
          border-radius: 8px;
          font-size: 1.2rem;
          line-height: 1.6;
          text-align: center;
        }

        .gap {
          display: inline-block;
          min-width: 80px;
          padding: 0.2rem 0.5rem;
          margin: 0 0.3rem;
          border: 2px solid #666;
          border-radius: 4px;
          cursor: pointer;
          text-align: center;
          transition: all 0.3s ease;
        }

        .gap.selected {
          border-color: #4CAF50;
          background: rgba(76, 175, 80, 0.1);
        }

        .gap.completed {
          border-color: #2196F3;
          background: rgba(33, 150, 243, 0.1);
          cursor: default;
        }

        .info-section {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .definition-box {
          background: rgba(0, 0, 0, 0.2);
          padding: 1rem;
          border-radius: 8px;
          margin-bottom: 1rem;
        }

        .definition-box h4 {
          margin: 0 0 0.5rem 0;
          color: #4CAF50;
        }

        .words-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
          gap: 1rem;
          padding: 1rem;
        }

        .word-card {
          background: rgba(255, 255, 255, 0.1);
          padding: 1rem;
          border-radius: 8px;
          cursor: pointer;
          text-align: center;
          transition: all 0.3s ease;
        }

        .word-card:hover:not(.matched) {
          background: rgba(255, 255, 255, 0.2);
        }

        .word-card.matched {
          opacity: 0.5;
          cursor: default;
        }
      `}</style>
    </div>
  );
}

export default WordCompletionGame;
