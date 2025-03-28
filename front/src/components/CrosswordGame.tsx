import { useEffect, useState } from 'react';
import { getVocabularyCrossword } from '../services/gameService';
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
  // For each placed word
  for (const placedWord of placedWords) {
    // For each letter in the placed word
    for (let i = 0; i < placedWord.word.length; i++) {
      // For each letter in the new word
      for (let j = 0; j < newWord.length; j++) {
        // If letters match
        if (placedWord.word[i] === newWord[j]) {
          let startX = 0;
          let startY = 0;
          const direction = placedWord.direction === 'across' ? 'down' as const : 'across' as const;

          // Calculate start position based on intersection
          if (placedWord.direction === 'across') {
            startX = placedWord.startX + i;
            startY = placedWord.startY - j;
          } else {
            startX = placedWord.startX - j;
            startY = placedWord.startY + i;
          }

          // Check if this placement would overlap with any existing words
          const isValidPlacement = !placedWords.some(word => {
            for (let k = 0; k < newWord.length; k++) {
              const x = direction === 'across' ? startX + k : startX;
              const y = direction === 'down' ? startY + k : startY;

              // Check if this position is used by another word with a different letter
              const overlappingWord = placedWords.find(w => {
                if (w === placedWord) return false;
                if (w.direction === 'across') {
                  return y === w.startY && x >= w.startX && x < w.startX + w.word.length &&
                         w.word[x - w.startX] !== newWord[k];
                } else {
                  return x === w.startX && y >= w.startY && y < w.startY + w.word.length &&
                         w.word[y - w.startY] !== newWord[k];
                }
              });

              if (overlappingWord) return true;
            }
            return false;
          });

          // If placement is valid, return it
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
  // Find minimum x and y coordinates
  let minX = 0;
  let minY = 0;
  words.forEach(word => {
    minX = Math.min(minX, word.startX);
    minY = Math.min(minY, word.startY);
  });

  // Shift all coordinates to be positive
  return words.map(word => ({
    ...word,
    startX: word.startX - minX,
    startY: word.startY - minY
  }));
};

interface WordWithDefinition {
  word: string;
  definition: string;
  difficulty: number;
}

const findValidCrossword = (wordPool: WordWithDefinition[]): Word[] => {
  const result: Word[] = [];
  let number = 1;

  // Try each word as the first word
  for (let i = 0; i < wordPool.length; i++) {
    result.length = 0;
    number = 1;

    // Place first word horizontally
    result.push({
      ...wordPool[i],
      direction: 'across',
      startX: 0,
      startY: 0,
      number: number++
    });

    // Try to add remaining words
    let remainingWords = [...wordPool.slice(0, i), ...wordPool.slice(i + 1)];
    let validLayout = false;

    // Try different combinations of remaining words
    for (let j = 0; j < remainingWords.length; j++) {
      const secondWord = remainingWords[j];
      const intersection1 = findIntersection(result, secondWord.word);
      
      if (intersection1) {
        result.push({
          ...secondWord,
          ...intersection1,
          number: number++
        });

        const remainingForThird = remainingWords.filter((_, idx) => idx !== j);
        
        // Try to find a third word
        for (let k = 0; k < remainingForThird.length; k++) {
          const thirdWord = remainingForThird[k];
          const intersection2 = findIntersection(result, thirdWord.word);

          if (intersection2) {
            result.push({
              ...thirdWord,
              ...intersection2,
              number: number++
            });

            const remainingForFourth = remainingForThird.filter((_, idx) => idx !== k);

            // Try to find a fourth word
            for (let l = 0; l < remainingForFourth.length; l++) {
              const fourthWord = remainingForFourth[l];
              const intersection3 = findIntersection(result, fourthWord.word);

              if (intersection3) {
                result.push({
                  ...fourthWord,
                  ...intersection3,
                  number: number++
                });
                validLayout = true;
                break;
              }
            }
          }
          
          if (validLayout) break;
          if (result.length > 2) result.length = 2; // Reset if third word didn't work
        }
      }
      
      if (validLayout) break;
      if (result.length > 1) result.length = 1; // Reset if second word didn't work
    }

    if (validLayout) break; // Found a valid layout with 4 words
  }

  if (result.length !== 4) {
    throw new Error("Could not create a valid crossword layout with 4 words");
  }

  return normalizeCoordinates(result);
};

const layoutCrossword = async (getNewWord: () => Promise<WordWithDefinition>): Promise<Word[]> => {
  // Get a pool of words first
  const wordPool: WordWithDefinition[] = [];
  for (let i = 0; i < 15; i++) {
    const response = await getNewWord();
    wordPool.push(response);
  }

  return findValidCrossword(wordPool);
};

function CrosswordGame({ enemyScore, onWin, onLose }: CrosswordGameProps) {
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

  // Check if a cell belongs to a completed word
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

  // Initialize new grid and words
  const initializeNewPuzzle = async () => {
    setLoading(true);
    setError(null);
    
    try {
      // Define function to get new words with definitions
      const getNewWord = async () => {
        const response = await getVocabularyCrossword();
        if (!response) throw new Error("Failed to fetch word");
        return { 
          word: response.word,
          definition: response.definition,
          difficulty: response.difficulty
        };
      };

      // Create layout for the crossword using word pool
      const wordSet = await layoutCrossword(getNewWord);

      setWords(wordSet);

      // Find grid dimensions (add 1 to ensure we have enough space)
      let maxX = 0;
      let maxY = 0;
      wordSet.forEach(word => {
        const endX = word.startX + (word.direction === 'across' ? word.word.length : 1);
        const endY = word.startY + (word.direction === 'down' ? word.word.length : 1);
        maxX = Math.max(maxX, endX);
        maxY = Math.max(maxY, endY);
      });

      // Create empty grid with active cell markers (add 1 to dimensions for safety)
      const newGrid: Cell[][] = Array(maxY + 1).fill(null).map(() => 
        Array(maxX + 1).fill(null).map(() => ({ letter: '', isActive: false }))
      );

      // Mark active cells and add numbers
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
      setSelectedWord(word);
      setCurrentCell({ x: word.startX, y: word.startY });
      setCurrentDirection(word.direction);
    }
  };

  const handleCellClick = (x: number, y: number) => {
    if (grid[y][x].isActive && !isCompletedCell(x, y)) {
      // Find word that contains this cell
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

  // Check if a word is complete and validate it
  const validateWord = (word: Word): boolean => {
    const enteredWord = Array.from({ length: word.word.length }, (_, i) => {
      const x = word.direction === 'across' ? word.startX + i : word.startX;
      const y = word.direction === 'down' ? word.startY + i : word.startY;
      return userInputs[`${x},${y}`] || '';
    }).join('');

    if (enteredWord === word.word) {
      const newCompleted = new Set(completedWords);
      newCompleted.add(word.word);
      setCompletedWords(newCompleted);

      // Calculate score based on difficulty
      const points = word.word.length * getPointsPerLetter(word.difficulty);
      setCurrentScore(prev => prev + points);

      // Update grid with correct word
      const newGrid = [...grid];
      for (let i = 0; i < word.word.length; i++) {
        const x = word.direction === 'across' ? word.startX + i : word.startX;
        const y = word.direction === 'down' ? word.startY + i : word.startY;
        newGrid[y][x].letter = word.word[i];
      }
      setGrid(newGrid);

      if (newCompleted.size === words.length) {
        if (currentScore > enemyScore) {
          onWin();
        } else {
          initializeNewPuzzle();
        }
      }

      return true;
    }
    return false;
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLDivElement>, x: number, y: number) => {
    if (!grid[y][x].isActive || isCompletedCell(x, y) || !selectedWord || completedWords.has(selectedWord.word)) return;

    if (/^[a-zA-Z]$/.test(e.key)) {
      const letter = e.key.toUpperCase();
      const cellKey = `${x},${y}`;
      
      setUserInputs(prev => ({ ...prev, [cellKey]: letter }));

      // Move to next cell or validate word if it's the last letter
      if (currentDirection) {
        const nextX = currentDirection === 'across' ? x + 1 : x;
        const nextY = currentDirection === 'down' ? y + 1 : y;
        const isLastCell = (currentDirection === 'across' && nextX === selectedWord.startX + selectedWord.word.length) ||
                          (currentDirection === 'down' && nextY === selectedWord.startY + selectedWord.word.length);

        if (isLastCell) {
          // Try to validate the word
          const isValid = validateWord(selectedWord);
          if (!isValid) {
            onLose();
          }
          setSelectedWord(null);
          setCurrentCell(null);
          setCurrentDirection(null);
        } else if (nextX < grid[0].length && nextY < grid.length && grid[nextY][nextX].isActive) {
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

  return (
    <div className="crossword-game">
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
