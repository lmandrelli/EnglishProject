import { useEffect, useState } from 'react';
import { getVocabularySynonyms, SynonymMatchItem } from '../services/gameService';
import Timer from './Timer';

// Using Fisher-Yates shuffle algorithm for better randomization
const shuffle = <T,>(array: T[]): T[] => {
  const newArray = [...array];
  for (let i = newArray.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
  }
  return newArray;
};

import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';

interface SynonymMatchGameProps {
  enemyScore: number;
  onWin: (score: number) => void;
  onLose: (score: number) => void;
  timeLimit?: number;
  currentScore?: number;
}

function SynonymMatchGame({ enemyScore, onWin, onLose, timeLimit = 120 }: SynonymMatchGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [synonymPairs, setSynonymPairs] = useState<SynonymMatchItem[]>([]);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [selectedWord, setSelectedWord] = useState<string | null>(null);
  const [selectedMatch, setSelectedMatch] = useState<string | null>(null);
  const [matchedPairs, setMatchedPairs] = useState<Set<string>>(new Set());
  const [shuffledWords, setShuffledWords] = useState<string[]>([]);
  const [shuffledSynonyms, setShuffledSynonyms] = useState<string[]>([]);
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
      const data = await getVocabularySynonyms(undefined, 5);
      setSynonymPairs(data);
      
      setShuffledWords(shuffle(data.map(item => item.word)));
      setShuffledSynonyms(shuffle(data.map(item => item.synonym)));
      
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

  const handleWordSelect = (word: string, side: 'word' | 'synonym') => {
    if (matchedPairs.has(word)) return;
    if (side === 'word') {
      setSelectedWord(word);
      setSelectedMatch(null);
    } else {
      setSelectedMatch(word);
      setSelectedWord(null);
    }
    if ((side === 'word' && selectedMatch) || (side === 'synonym' && selectedWord)) {
      const baseWord = side === 'word' ? word : selectedWord;
      const synonymWord = side === 'synonym' ? word : selectedMatch;
      
      const isMatch = synonymPairs.some(
        item => item.word === baseWord && item.synonym === synonymWord
      );
      if (isMatch) {
        const newMatchedPairs = new Set(matchedPairs);
        newMatchedPairs.add(baseWord as string);
        newMatchedPairs.add(synonymWord as string);
        setMatchedPairs(newMatchedPairs);
        
        const matchedItem = synonymPairs.find(
          item => item.word === baseWord && item.synonym === synonymWord
        );
        
        let difficultyScore;
        if (matchedItem?.difficulty === 1) {
          difficultyScore = 50;
        } else if (matchedItem?.difficulty === 2) {
          difficultyScore = 75;
        } else {
          difficultyScore = 150;
        }
        setCurrentScore(prevScore => prevScore + difficultyScore);
        
        if (newMatchedPairs.size === synonymPairs.length * 2) {
          if (currentScore + difficultyScore > enemyScore) {
            setTimeout(handleVictory, 500);
          } else {
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
        <h3>Match words with their synonyms!</h3>
        <p>Click a word from each column to make a match.</p>
      </div>
      
      <div className="regional-variants-game synonym-match-game">
        <div className="column-header">
          <h3>Words</h3>
        </div>
        
        <div className="column-header">
          <h3>Synonyms</h3>
        </div>
        
        <div className="words-column">
          {shuffledWords.map((word, index) => (
            <div 
              key={`word-${index}`}
              className={`word-card ${matchedPairs.has(word) ? 'matched' : ''} ${selectedWord === word ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(word) && handleWordSelect(word, 'word')}
            >
              {word}
            </div>
          ))}
        </div>
        
        <div className="words-column">
          {shuffledSynonyms.map((word, index) => (
            <div 
              key={`synonym-${index}`}
              className={`word-card ${matchedPairs.has(word) ? 'matched' : ''} ${selectedMatch === word ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(word) && handleWordSelect(word, 'synonym')}
            >
              {word}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default SynonymMatchGame;
