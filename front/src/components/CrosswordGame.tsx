import { useEffect, useState } from 'react';
import { getVocabularyCrossword } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import './CrosswordGame.css';

interface Word {
  word: string;
  definition: string;
  direction: 'across' | 'down';
  startX: number;
  startY: number;
  number: number;
  difficulty: number;
}

interface Cell {
  letter: string;
  isActive: boolean;
  number?: number;
  isSelected?: boolean;
}

interface CrosswordGameProps {
  enemyScore: number;
  onWin: () => void;
  onLose: () => void;
  wordCount?: number;
  timeLimit?: number; // Time limit in seconds (default: 180)
}

interface WordWithDefinition {
  word: string;
  definition: string;
  difficulty: number;
}

const getPointsPerLetter = (difficulty: number): number => {
  switch (difficulty) {
    case 1: return 1;
    case 2: return 2;
    case 3: return 3;
    default: return 1;
  }
};

const findIntersection = (placedWords: Word[], newWord: string): { startX: number; startY: number; direction: 'across' | 'down' } | null => {
  for (const placedWord of placedWords) {
    for (let i = 1; i < placedWord.word.length; i++) {
      for (let j = 1; j < newWord.length; j++) {
        if (placedWord.word[i] === newWord[j]) {
          let startX = 0;
          let startY = 0;
          const direction = placedWord.direction === 'across' ? 'down' as const : 'across' as const;

          if (placedWord.direction === 'across') {
            startX = placedWord.startX + i;
            startY = placedWord.startY - j;
          } else {
            startX = placedWord.startX - j;
            startY = placedWord.startY + i;
          }

          const isValidPlacement = !placedWords.some(word => {
            for (let k = -1; k <= newWord.length; k++) {
              const x = direction === 'across' ? startX + k : startX;
              const y = direction === 'down' ? startY + k : startY;

              for (let dy = -1; dy <= 1; dy++) {
                for (let dx = -1; dx <= 1; dx++) {
                  if (dx === 0 && dy === 0) continue;
                  const checkX = x + dx;
                  const checkY = y + dy;

                  const adjacentWord = placedWords.find(w => {
                    if (w === placedWord) return false;
                    if (w.direction === 'across') {
                      return checkY === w.startY && 
                             checkX >= w.startX && 
                             checkX < w.startX + w.word.length &&
                             !(y === w.startY && x === w.startX + i);
                    } else {
                      return checkX === w.startX && 
                             checkY >= w.startY && 
                             checkY < w.startY + w.word.length &&
                             !(x === w.startX && y === w.startY + i);
                    }
                  });

                  if (adjacentWord) return true;
                }
              }
            }
            return false;
          });

          if (isValidPlacement) {
            return { startX, startY, direction };
          }
        }
      }
    }
  }
  return null;
};

const normalizeCoordinates = (words: Word[]): Word[] => {
  let minX = 0;
  let minY = 0;
  words.forEach(word => {
    minX = Math.min(minX, word.startX);
    minY = Math.min(minY, word.startY);
  });

  return words.map(word => ({
    ...word,
    startX: word.startX - minX,
    startY: word.startY - minY
  }));
};

const findValidCrossword = (wordPool: WordWithDefinition[], targetWordCount: number): Word[] => {
  const result: Word[] = [];
  let number = 1;

  for (let i = 0; i < wordPool.length; i++) {
    result.length = 0;
    number = 1;

    result.push({
      ...wordPool[i],
      direction: 'across',
      startX: 0,
      startY: 0,
      number: number++
    });

    let remainingWords = [...wordPool.slice(0, i), ...wordPool.slice(i + 1)];
    let validLayout = false;

    const tryAddWord = (currentWords: Word[], remaining: WordWithDefinition[]): boolean => {
      if (currentWords.length === targetWordCount) {
        const acrossCount = currentWords.filter(w => w.direction === 'across').length;
        return acrossCount >= Math.ceil(targetWordCount / 2);
      }

      const currentAcrossCount = currentWords.filter(w => w.direction === 'across').length;
      const remainingWords = targetWordCount - currentWords.length;
      const minAcrossNeeded = Math.ceil(targetWordCount / 2) - currentAcrossCount;
      
      for (let j = 0; j < remaining.length; j++) {
        const nextWord = remaining[j];
        const intersection = findIntersection(currentWords, nextWord.word);

        if (intersection) {
          if (minAcrossNeeded > 0 && intersection.direction === 'down' && 
              remainingWords - 1 < minAcrossNeeded) {
            continue;
          }

          currentWords.push({
            ...nextWord,
            ...intersection,
            number: number++
          });

          const newRemaining = remaining.filter((_, idx) => idx !== j);
          if (tryAddWord(currentWords, newRemaining)) {
            return true;
          }

          currentWords.pop();
          number--;
        }
      }

      return false;
    };

    validLayout = tryAddWord(result, remainingWords);
    if (validLayout) break;
  }

  if (result.length !== targetWordCount) {
    throw new Error(`Could not create a valid crossword layout with ${targetWordCount} words`);
  }

  return normalizeCoordinates(result);
};

const layoutCrossword = async (getNewWord: () => Promise<WordWithDefinition>, wordCount: number): Promise<Word[]> => {
  const wordPool: WordWithDefinition[] = [];
  const usedWords = new Set<string>();

  while (wordPool.length < wordCount) {
    const response = await getNewWord();
    if (!usedWords.has(response.word.toLowerCase())) {
      wordPool.push(response);
      usedWords.add(response.word.toLowerCase());
    }
  }

  return findValidCrossword(wordPool, wordCount);
};

function CrosswordGame({ enemyScore, onWin, onLose, wordCount = 4, timeLimit = 180 }: CrosswordGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [words, setWords] = useState<Word[]>([]);
  const [grid, setGrid] = useState<Cell[][]>([]);
  const [selectedWord, setSelectedWord] = useState<Word | null>(null);
  const [currentCell, setCurrentCell] = useState<{ x: number, y: number } | null>(null);
  const [currentDirection, setCurrentDirection] = useState<'across' | 'down' | null>(null);
  const [userInputs, setUserInputs] = useState<{ [key: string]: string }>({});
  const [completedWords, setCompletedWords] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showWinAnimation, setShowWinAnimation] = useState(false);

  const isCompletedCell = (x: number, y: number): boolean => {
    const cellCompletedWords = words.filter(word => {
      if (word.direction === 'across') {
        return y === word.startY && x >= word.startX && x < word.startX + word.word.length;
      } else {
        return x === word.startX && y >= word.startY && y < word.startY + word.word.length;
      }
    });

    return cellCompletedWords.some(word => completedWords.has(word.word));
  };

  const checkWordCompletion = (word: Word) => {
    if (completedWords.has(word.word)) return false;

    const isComplete = Array.from({ length: word.word.length }, (_, i) => {
      const x = word.direction === 'across' ? word.startX + i : word.startX;
      const y = word.direction === 'down' ? word.startY + i : word.startY;
      return userInputs[`${x},${y}`] || '';
    }).every(letter => letter !== '');

    if (isComplete) {
      const isValid = validateWord(word);
      
      if (isValid) {
        setSelectedWord(null);
        setCurrentCell(null);
        setCurrentDirection(null);
      } else {
        // Reset word cells and mark them red
        for (let i = 0; i < word.word.length; i++) {
          const x = word.direction === 'across' ? word.startX + i : word.startX;
          const y = word.direction === 'down' ? word.startY + i : word.startY;
          const cellKey = `${x},${y}`;
          setUserInputs(prev => {
            const newInputs = { ...prev };
            delete newInputs[cellKey];
            return newInputs;
          });

          const cell = document.querySelector(`[data-position="${x},${y}"]`) as HTMLElement;
          if (cell) {
            cell.classList.add('incorrect');
            setTimeout(() => cell.classList.remove('incorrect'), 1000);
          }
        }
      }
    }
  };

  const validateWord = (word: Word): boolean => {
    const enteredWord = Array.from({ length: word.word.length }, (_, i) => {
      const x = word.direction === 'across' ? word.startX + i : word.startX;
      const y = word.direction === 'down' ? word.startY + i : word.startY;
      return userInputs[`${x},${y}`] || '';
    }).join('');

    console.log('🔍 Validating word:', {
      entered: enteredWord,
      expected: word.word,
      matches: enteredWord === word.word
    });

    if (enteredWord === word.word) {
      const newCompleted = new Set(completedWords);
      newCompleted.add(word.word);
      setCompletedWords(newCompleted);

      const points = word.word.length * getPointsPerLetter(word.difficulty);
      const newScore = currentScore + points;
      console.log('📈 Updating score:', {
        points,
        newScore,
        difficulty: word.difficulty
      });
      setCurrentScore(newScore);

      const newGrid = [...grid];
      for (let i = 0; i < word.word.length; i++) {
        const x = word.direction === 'across' ? word.startX + i : word.startX;
        const y = word.direction === 'down' ? word.startY + i : word.startY;
        newGrid[y][x].letter = word.word[i];
      }
      setGrid(newGrid);

      if (newCompleted.size === words.length) {
        console.log('🎯 All words completed!', {
          finalScore: newScore,
          enemyScore,
          win: newScore >= enemyScore
        });
        if (newScore >= enemyScore) {
          const gridElement = document.querySelector('.grid') as HTMLElement;
          if (gridElement) {
            gridElement.classList.add('winning-grid');
          setTimeout(() => {
            setShowWinAnimation(true);
          }, 1000);
          }
        } else {
          initializeNewPuzzle();
        }
      }

      return true;
    }
    return false;
  };

  const initializeNewPuzzle = async () => {
    setLoading(true);
    setError(null);
    
    try {
      console.log('🔄 Initializing new puzzle');
      const getNewWord = async () => {
        const response = await getVocabularyCrossword();
        if (!response) throw new Error("Failed to fetch word");
        return { 
          word: response.word,
          definition: response.definition,
          difficulty: response.difficulty
        };
      };

      const wordSet = await layoutCrossword(getNewWord, wordCount);
      console.log('📝 Generated crossword layout:', wordSet);
      setWords(wordSet);

      let maxX = 0;
      let maxY = 0;
      wordSet.forEach(word => {
        const endX = word.startX + (word.direction === 'across' ? word.word.length : 1);
        const endY = word.startY + (word.direction === 'down' ? word.word.length : 1);
        maxX = Math.max(maxX, endX);
        maxY = Math.max(maxY, endY);
      });

      const newGrid: Cell[][] = Array(maxY + 1).fill(null).map(() => 
        Array(maxX + 1).fill(null).map(() => ({ letter: '', isActive: false }))
      );

      wordSet.forEach(word => {
        for (let i = 0; i < word.word.length; i++) {
          const x = word.direction === 'across' ? word.startX + i : word.startX;
          const y = word.direction === 'down' ? word.startY + i : word.startY;
          
          newGrid[y][x].isActive = true;
          if (i === 0) {
            newGrid[y][x].number = word.number;
          }
        }
      });

      setGrid(newGrid);
      setCompletedWords(new Set());
      setUserInputs({});
      setSelectedWord(null);
      setCurrentCell(null);
      setCurrentDirection(null);
      console.log('✨ New puzzle initialized');
    } catch (err) {
      console.error("Error initializing puzzle:", err);
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    initializeNewPuzzle().catch(console.error);
  }, []);

  const handleWordSelect = (word: Word) => {
    if (!completedWords.has(word.word)) {
      console.log('👆 Word selected:', {
        word: word.word,
        direction: word.direction,
        number: word.number
      });
      setSelectedWord(word);
      setCurrentCell({ x: word.startX, y: word.startY });
      setCurrentDirection(word.direction);
    }
  };

  const handleCellClick = (x: number, y: number) => {
    if (grid[y][x].isActive && !isCompletedCell(x, y)) {
      const word = words.find(w => {
        if (w.direction === 'across') {
          return y === w.startY && x >= w.startX && x < w.startX + w.word.length;
        } else {
          return x === w.startX && y >= w.startY && y < w.startY + w.word.length;
        }
      });

      if (word && !completedWords.has(word.word)) {
        setSelectedWord(word);
        setCurrentCell({ x, y });
        setCurrentDirection(word.direction);
      }
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLDivElement>, x: number, y: number) => {
    if (!grid[y][x].isActive || isCompletedCell(x, y) || !selectedWord || completedWords.has(selectedWord.word)) return;

    if (/^[a-zA-Z]$/.test(e.key)) {
      const letter = e.key.toUpperCase();
      const cellKey = `${x},${y}`;
      
      console.log('⌨️ Key pressed:', {
        letter,
        position: { x, y },
        word: selectedWord.word,
        currentCompletion: userInputs
      });

      setUserInputs(prev => {
        const newInputs = { ...prev, [cellKey]: letter };
        
        // After updating inputs, check word completion
        setTimeout(() => {
          checkWordCompletion(selectedWord);
        }, 0);
        
        return newInputs;
      });

      // Move to next cell
      if (currentDirection) {
        const nextX = currentDirection === 'across' ? x + 1 : x;
        const nextY = currentDirection === 'down' ? y + 1 : y;

        // Only move to next cell if within grid bounds and cell is active
        if (nextX < grid[0].length && nextY < grid.length && grid[nextY][nextX].isActive) {
          setCurrentCell({ x: nextX, y: nextY });
        }
      }
    }
  };

  useEffect(() => {
    if (currentCell) {
      const cellElement = document.querySelector(
        `[data-position="${currentCell.x},${currentCell.y}"]`
      ) as HTMLElement;
      if (cellElement) {
        cellElement.focus();
      }
    }
  }, [currentCell]);

  const handleNextRound = () => {
    setShowWinAnimation(false);
    onWin();
  };

  const handleTimeUp = () => {
    onLose();
  };

  return (
    <div className="crossword-game">
      {showWinAnimation && <WinAnimation onNextRound={handleNextRound} />}
      <Timer duration={timeLimit} onTimeUp={handleTimeUp} />
      <div className="score-display">
        Score: {currentScore} / Enemy Score: {enemyScore}
      </div>

      {error && (
        <div className="error-message">
          {error}
          <button onClick={() => initializeNewPuzzle()}>Try Again</button>
        </div>
      )}
      
      {loading ? (
        <div className="loading">Loading puzzle...</div>
      ) : (
        <div className="game-area">
          <div className="grid">
            {grid.map((row, y) => (
              <div key={y} className="grid-row">
                {row.map((cell, x) => (
                  <div 
                    key={`${x}-${y}`} 
                    className={`grid-cell ${cell.isActive ? 'active' : ''} ${
                      currentCell?.x === x && currentCell?.y === y ? 'selected' : ''
                    } ${isCompletedCell(x, y) ? 'completed' : ''}`}
                    onClick={() => handleCellClick(x, y)}
                    onKeyDown={(e) => handleKeyPress(e, x, y)}
                    tabIndex={cell.isActive && !isCompletedCell(x, y) ? 0 : -1}
                    data-position={`${x},${y}`}
                  >
                    {cell.number && <span className="cell-number">{cell.number}</span>}
                    {cell.isActive ? (userInputs[`${x},${y}`] || cell.letter) : null}
                  </div>
                ))}
              </div>
            ))}
          </div>

          <div className="clues">
            <h3>Clues</h3>
            {words.map((word, index) => (
              <div
                key={index}
                className={`clue ${completedWords.has(word.word) ? 'completed' : ''} ${selectedWord === word ? 'selected' : ''}`}
                onClick={() => handleWordSelect(word)}
              >
                <span className="direction">{word.number}. {word.direction.toUpperCase()}</span>
                <span className="definition">{word.definition}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default CrosswordGame;
