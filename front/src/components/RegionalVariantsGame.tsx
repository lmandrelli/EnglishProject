import { useEffect, useState } from 'react';
import { getCultureRegionalVariants, RegionalVariantItem } from '../services/gameService';
import './CultureGames.css';

interface RegionalVariantsGameProps {
  enemyScore: number;
  onWin: () => void;
  onLose: () => void;
}

function RegionalVariantsGame({ enemyScore, onWin, onLose }: RegionalVariantsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [regionalVariants, setRegionalVariants] = useState<RegionalVariantItem[]>([]);
  const [selectedWord, setSelectedWord] = useState<string | null>(null);
  const [selectedMatch, setSelectedMatch] = useState<string | null>(null);
  const [matchedPairs, setMatchedPairs] = useState<Set<string>>(new Set());
  const [attempts, setAttempts] = useState(0);
  const [shuffledUK, setShuffledUK] = useState<string[]>([]);
  const [shuffledUS, setShuffledUS] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const data = await getCultureRegionalVariants(undefined, 5);
        setRegionalVariants(data);
        
        setShuffledUK(data.map(item => item.uk_word).sort(() => Math.random() - 0.5));
        setShuffledUS(data.map(item => item.us_word).sort(() => Math.random() - 0.5));
        
        setLoading(false);
      } catch (err) {
        setError('Failed to load game data');
        setLoading(false);
        console.error(err);
      }
    };

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
        setCurrentScore(prevScore => prevScore + 200);
        
        if (newMatchedPairs.size === regionalVariants.length * 2) {
          if (currentScore + 200 > enemyScore) {
            onWin();
          } else {
            onLose();
          }
        }
      } else {
        setAttempts(prev => prev + 1);
        setCurrentScore(prevScore => Math.max(0, prevScore - 50));
        
        if (attempts >= 5) {
          onLose();
        }
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

  if (loading) {
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
        <h3>Match British English words with their American English equivalents!</h3>
        <p>Click a word from each column to make a match. You have {5 - attempts} attempts remaining.</p>
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