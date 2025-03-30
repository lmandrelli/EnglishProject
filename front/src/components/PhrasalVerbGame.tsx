import { useEffect, useState } from 'react';
import { getGrammarPhrasalVerbs, PhrasalVerbItem } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';

interface PhrasalVerbGameProps {
  enemyScore: number;
  onWin: (score: number) => void;
  onLose: (score: number) => void;
  timeLimit?: number;
  currentScore?: number;
}

function PhrasalVerbGame({ enemyScore, onWin, onLose, timeLimit = 120 }: PhrasalVerbGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [phrasalVerbs, setPhrasalVerbs] = useState<PhrasalVerbItem[]>([]);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [selectedVerbIndex, setSelectedVerbIndex] = useState<number | null>(null);
  const [selectedParticle, setSelectedParticle] = useState<string | null>(null);
  const [matchedPairs, setMatchedPairs] = useState<Set<number>>(new Set());
  const [uniqueParticles, setUniqueParticles] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);
  const [hasWon, setHasWon] = useState(false);
  const [winAnimationKey, setWinAnimationKey] = useState(0);

  const handleVictory = () => {
    if (!hasWon) {
      setHasWon(true);
      setShowWinAnimation(true);
      setWinAnimationKey(prev => prev + 1);
    }
  };

  const fetchData = async () => {
    try {
      setLoading(true);
      const data = await getGrammarPhrasalVerbs(undefined, 5);
      setPhrasalVerbs(data);
      
      // Get unique particles and shuffle them
      const uniqueParticlesList = Array.from(new Set(data.map(item => item.particle)))
        .sort(() => Math.random() - 0.5);
      setUniqueParticles(uniqueParticlesList);
      
      setMatchedPairs(new Set());
      setSelectedVerbIndex(null);
      setSelectedParticle(null);
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

  const handleSelect = (index: number | string, type: 'verb' | 'particle') => {
    if (type === 'verb') {
      const verbIndex = index as number;
      if (matchedPairs.has(verbIndex)) return;
      setSelectedVerbIndex(verbIndex);
      setSelectedParticle(null);
    } else {
      const particle = index as string;
      setSelectedParticle(particle);
      setSelectedVerbIndex(null);
    }

    if ((type === 'verb' && selectedParticle) || (type === 'particle' && selectedVerbIndex !== null)) {
      const verbIndex = type === 'verb' ? index as number : selectedVerbIndex;
      const particle = type === 'particle' ? index as string : selectedParticle;

      if (verbIndex === null) return;

      const isMatch = phrasalVerbs[verbIndex].particle === particle;

      if (isMatch) {
        const newMatchedPairs = new Set(matchedPairs);
        newMatchedPairs.add(verbIndex);
        setMatchedPairs(newMatchedPairs);
        
        const matchedItem = phrasalVerbs[verbIndex];
        
        let difficultyScore;
        if (matchedItem.difficulty === 1) {
          difficultyScore = 100;
        } else if (matchedItem.difficulty === 2) {
          difficultyScore = 150;
        } else {
          difficultyScore = 300;
        }
        setCurrentScore(prevScore => prevScore + difficultyScore);
        
        if (newMatchedPairs.size === phrasalVerbs.length) {
          if (currentScore + difficultyScore > enemyScore) {
            setHasWon(true);
            setShowWinAnimation(true);
          } else {
            fetchData();
          }
        }
      } else {
        setCurrentScore(prevScore => Math.max(0, prevScore - 50));
      }
      
      setSelectedVerbIndex(null);
      setSelectedParticle(null);
    }
  };

  const handleTimeUp = () => {
    if (!hasWon && currentScore > enemyScore) {
      setHasWon(true);
      setShowWinAnimation(true);
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

  // Helper function to get the count of a particle's usage in matched pairs
  const getParticleMatchCount = (particle: string): number => {
    return [...matchedPairs].reduce((count, verbIndex) => {
      return phrasalVerbs[verbIndex].particle === particle ? count + 1 : count;
    }, 0);
  };

  // Helper function to get the total expected matches for a particle
  const getParticleTotalCount = (particle: string): number => {
    return phrasalVerbs.filter(verb => verb.particle === particle).length;
  };

  if (loading) {
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
        <h3>Match base verbs with their particles!</h3>
        <p>Click a base verb on the left and match it with its correct particle on the right.</p>
      </div>
      
      <div className="regional-variants-game">
        <div className="column-header">
          <h3>Base Verbs</h3>
        </div>
        
        <div className="column-header">
          <h3>Particles</h3>
        </div>
        
        <div className="words-column">
          {phrasalVerbs.map((item, index) => (
            <div 
              key={`verb-${index}`}
              className={`word-card verb-card ${matchedPairs.has(index) ? 'matched' : ''} ${selectedVerbIndex === index ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(index) && handleSelect(index, 'verb')}
            >
              <div className="verb-content">
                <strong>{item.verb}</strong>
                <span className="meaning">{item.meaning}</span>
              </div>
            </div>
          ))}
        </div>
        
        <div className="words-column">
          {uniqueParticles.map((particle, index) => {
            const matchCount = getParticleMatchCount(particle);
            const totalCount = getParticleTotalCount(particle);
            return (
              <div 
                key={`particle-${index}`}
                className={`word-card particle-card ${matchCount === totalCount ? 'matched' : ''} ${selectedParticle === particle ? 'selected' : ''}`}
                onClick={() => matchCount < totalCount && handleSelect(particle, 'particle')}
              >
                <span className="particle-text">{particle}</span>
                {totalCount > 1 && (
                  <span className="particle-count">
                    {matchCount}/{totalCount}
                  </span>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <style>{`
        .verb-card {
          text-align: left;
          padding: 10px;
        }
        
        .verb-content {
          display: flex;
          flex-direction: column;
          gap: 5px;
        }
        
        .verb-content strong {
          font-size: 1.2em;
          color:rgb(255, 255, 255);
        }
        
        .verb-content .meaning {
          font-size: 0.9em;
          color:rgb(192, 192, 192);
          font-style: italic;
        }

        .particle-card {
          display: flex;
          justify-content: center;
          align-items: center;
          gap: 10px;
          font-size: 1.2em;
          font-weight: bold;
          color:rgb(255, 255, 255);
          padding: 10px;
        }

        .particle-text {
          flex: 1;
          text-align: center;
        }

        .particle-count {
          font-size: 0.8em;
          color:rgb(145, 145, 145);
          min-width: 30px;
        }

        .matched.particle-card {
          opacity: 0.5;
        }
      `}</style>
    </div>
  );
}

export default PhrasalVerbGame;
