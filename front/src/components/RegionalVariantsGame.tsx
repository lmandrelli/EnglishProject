import { useEffect, useState } from 'react';
import { getCultureRegionalVariants, RegionalVariantItem } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';

interface RegionalVariantsGameProps {
  enemyScore: number;
  onWin: (score: number) => void;
  onLose: (score: number) => void;
  timeLimit?: number; // Time limit in seconds (default: 120)
  currentScore?: number;
}

function RegionalVariantsGame({ enemyScore, onWin, onLose, timeLimit = 120 }: RegionalVariantsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [regionalVariants, setRegionalVariants] = useState<RegionalVariantItem[]>([]);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [selectedWord, setSelectedWord] = useState<string | null>(null);
  const [selectedMatch, setSelectedMatch] = useState<string | null>(null);
  const [matchedPairs, setMatchedPairs] = useState<Set<string>>(new Set());
  const [shuffledUK, setShuffledUK] = useState<string[]>([]);
  const [shuffledUS, setShuffledUS] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);

  const fetchData = async () => {
    try {
      setLoading(true);
      const data = await getCultureRegionalVariants(undefined, 5);
      setRegionalVariants(data);
      
      setShuffledUK(data.map(item => item.uk_word).sort(() => Math.random() - 0.5));
      setShuffledUS(data.map(item => item.us_word).sort(() => Math.random() - 0.5));
      
      setMatchedPairs(new Set());
      setSelectedWord(null);
      setSelectedMatch(null);
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

  const handleWordSelect = (word: string, side: 'uk' | 'us') => {
    if (matchedPairs.has(word)) return;
    if (side === 'uk') {
      setSelectedWord(word);
      setSelectedMatch(null);
    } else {
      setSelectedMatch(word);
      setSelectedWord(null);
    }
    if ((side === 'uk' && selectedMatch) || (side === 'us' && selectedWord)) {
      const ukWord = side === 'uk' ? word : selectedWord;
      const usWord = side === 'us' ? word : selectedMatch;
      
      const isMatch = regionalVariants.some(
        item => item.uk_word === ukWord && item.us_word === usWord
      );
      if (isMatch) {
        const newMatchedPairs = new Set(matchedPairs);
        newMatchedPairs.add(ukWord as string);
        newMatchedPairs.add(usWord as string);
        setMatchedPairs(newMatchedPairs);
        // Find the matched item to get its difficulty level
        const matchedItem = regionalVariants.find(
          item => item.uk_word === ukWord && item.us_word === usWord
        );
        // Score based on difficulty level
        let difficultyScore;
        if (matchedItem?.difficulty === 1) {
          difficultyScore = 100;
        } else if (matchedItem?.difficulty === 2) {
          difficultyScore = 150;
        } else {
          difficultyScore = 300;
        }
        setCurrentScore(prevScore => prevScore + difficultyScore);
        
        // Vérifier si toutes les paires ont été associées
        if (newMatchedPairs.size === regionalVariants.length * 2) {
          // Vérifier si le score est suffisant pour gagner
          if (currentScore + difficultyScore > enemyScore) {
            setTimeout(() => {
              setShowWinAnimation(true);
            }, 500);
          } else {
            // Recharger le jeu avec un nouveau set de mots
            fetchData();
          }
        }
      } else {
        setCurrentScore(prevScore => Math.max(0, prevScore - 50));
      }
      
      setSelectedWord(null);
      setSelectedMatch(null);
    }
  };

  const getMeaning = (word: string): string => {
    const variant = regionalVariants.find(
      item => item.uk_word === word || item.us_word === word
    );
    return variant ? variant.meaning : '';
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
    onWin(currentScore);
  };

  const handleReturnToMenu = () => {
    setShowLoseOverlay(false);
    onLose(currentScore);
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
        <h3>Match British English words with their American English equivalents!</h3>
        <p>Click a word from each column to make a match.</p>
      </div>
      
      <div className="regional-variants-game">
        <div className="column-header uk">
          <div className="flag uk-flag"></div>
          <h3>British English</h3>
        </div>
        
        <div className="column-header us">
          <div className="flag us-flag"></div>
          <h3>American English</h3>
        </div>
        
        <div className="words-column uk-words">
          {shuffledUK.map((word, index) => (
            <div 
              key={`uk-${index}`}
              className={`word-card ${matchedPairs.has(word) ? 'matched' : ''} ${selectedWord === word ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(word) && handleWordSelect(word, 'uk')}
            >
              {word}
              {matchedPairs.has(word) && (
                <div className="meaning-tooltip">{getMeaning(word)}</div>
              )}
            </div>
          ))}
        </div>
        
        <div className="words-column us-words">
          {shuffledUS.map((word, index) => (
            <div 
              key={`us-${index}`}
              className={`word-card ${matchedPairs.has(word) ? 'matched' : ''} ${selectedMatch === word ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(word) && handleWordSelect(word, 'us')}
            >
              {word}
              {matchedPairs.has(word) && (
                <div className="meaning-tooltip">{getMeaning(word)}</div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default RegionalVariantsGame;
