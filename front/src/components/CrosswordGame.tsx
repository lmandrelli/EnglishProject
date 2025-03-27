import { useEffect, useState } from 'react';
import './CrosswordGame.css';

interface Word {
  word: string;
  definition: string;
  direction: 'across' | 'down';
  startX: number;
  startY: number;
  number: number;
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

// FIXME: Replace with API data
const WORD_SETS: Word[][] = [
  [
    { word: 'HELLO', definition: 'A greeting', direction: 'across' as const, startX: 0, startY: 0, number: 1 },
    { word: 'HELP', definition: 'To assist someone', direction: 'down' as const, startX: 0, startY: 0, number: 1 },
    { word: 'WORLD', definition: 'The planet Earth', direction: 'down' as const, startX: 4, startY: 0, number: 2 },
  ],
  [
    { word: 'LEARN', definition: 'To gain knowledge', direction: 'across' as const, startX: 0, startY: 0, number: 1 },
    { word: 'LOVE', definition: 'Strong affection', direction: 'down' as const, startX: 2, startY: 0, number: 2 },
    { word: 'NEW', definition: 'Not old', direction: 'across' as const, startX: 0, startY: 2, number: 3 },
  ],
  [
    { word: 'DREAM', definition: 'Images during sleep', direction: 'across' as const, startX: 0, startY: 1, number: 2 },
    { word: 'DARK', definition: 'Without light', direction: 'down' as const, startX: 0, startY: 1, number: 1 },
    { word: 'MAY', definition: 'Fifth month', direction: 'down' as const, startX: 2, startY: 1, number: 3 },
  ]
];

function CrosswordGame({ enemyScore, onWin, onLose }: CrosswordGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [words, setWords] = useState<Word[]>([]);
  const [grid, setGrid] = useState<Cell[][]>([]);
  const [selectedWord, setSelectedWord] = useState<Word | null>(null);
  const [currentCell, setCurrentCell] = useState<{ x: number, y: number } | null>(null);
  const [currentDirection, setCurrentDirection] = useState<'across' | 'down' | null>(null);
  const [userInputs, setUserInputs] = useState<{ [key: string]: string }>({});
  const [completedWords, setCompletedWords] = useState<Set<string>>(new Set());

  // Initialize new grid and words
  const initializeNewPuzzle = () => {
    const wordSet = WORD_SETS[Math.floor(Math.random() * WORD_SETS.length)];
    setWords(wordSet);
    
    // Find grid dimensions
    let maxX = 0;
    let maxY = 0;
    wordSet.forEach(word => {
      const endX = word.startX + (word.direction === 'across' ? word.word.length : 1);
      const endY = word.startY + (word.direction === 'down' ? word.word.length : 1);
      maxX = Math.max(maxX, endX);
      maxY = Math.max(maxY, endY);
    });

    // Create empty grid with active cell markers
    const newGrid: Cell[][] = Array(maxY).fill(null).map(() => 
      Array(maxX).fill(null).map(() => ({ letter: '', isActive: false }))
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
  };

  useEffect(() => {
    initializeNewPuzzle();
  }, []);

  const handleWordSelect = (word: Word) => {
    if (!completedWords.has(word.word)) {
      setSelectedWord(word);
      setCurrentCell({ x: word.startX, y: word.startY });
      setCurrentDirection(word.direction);
    }
  };

  const handleCellClick = (x: number, y: number) => {
    if (grid[y][x].isActive) {
      // Find word that contains this cell
      const word = words.find(w => {
        if (w.direction === 'across') {
          return y === w.startY && x >= w.startX && x < w.startX + w.word.length;
        } else {
          return x === w.startX && y >= w.startY && y < w.startY + w.word.length;
        }
      });

      if (word) {
        setSelectedWord(word);
        setCurrentCell({ x, y });
        setCurrentDirection(word.direction);
      }
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLDivElement>, x: number, y: number) => {
    if (!grid[y][x].isActive || completedWords.has(selectedWord?.word || '')) return;

    if (/^[a-zA-Z]$/.test(e.key)) {
      const letter = e.key.toUpperCase();
      const cellKey = `${x},${y}`;
      
      setUserInputs(prev => ({ ...prev, [cellKey]: letter }));

      // Move to next cell
      if (currentDirection && selectedWord) {
        const nextX = currentDirection === 'across' ? x + 1 : x;
        const nextY = currentDirection === 'down' ? y + 1 : y;

        if (
          nextX < grid[0].length && 
          nextY < grid.length && 
          grid[nextY][nextX].isActive
        ) {
          setCurrentCell({ x: nextX, y: nextY });
        }

        // Check if word is complete
        const getWordCells = () => {
          const cells: string[] = [];
          for (let i = 0; i < selectedWord.word.length; i++) {
            const checkX = selectedWord.direction === 'across' ? selectedWord.startX + i : selectedWord.startX;
            const checkY = selectedWord.direction === 'down' ? selectedWord.startY + i : selectedWord.startY;
            const cellKey = `${checkX},${checkY}`;
            cells.push(userInputs[cellKey] || '');
          }
          return cells;
        };

        const wordCells = getWordCells();
        if (!wordCells.includes('')) {
          const enteredWord = wordCells.join('');
          if (enteredWord === selectedWord.word) {
            const newCompleted = new Set(completedWords);
            newCompleted.add(selectedWord.word);
            setCompletedWords(newCompleted);
            setCurrentScore(prev => prev + selectedWord.word.length * 100);

            // Update grid with correct word
            const newGrid = [...grid];
            for (let i = 0; i < selectedWord.word.length; i++) {
              if (selectedWord.direction === 'across') {
                newGrid[selectedWord.startY][selectedWord.startX + i].letter = selectedWord.word[i];
              } else {
                newGrid[selectedWord.startY + i][selectedWord.startX].letter = selectedWord.word[i];
              }
            }
            setGrid(newGrid);

            if (newCompleted.size === words.length) {
              if (currentScore > enemyScore) {
                onWin();
              } else {
                initializeNewPuzzle();
              }
            }

            setSelectedWord(null);
            setCurrentCell(null);
            setCurrentDirection(null);
          } else {
            onLose();
          }
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
      
      <div className="game-area">
        <div className="grid">
          {grid.map((row, y) => (
            <div key={y} className="grid-row">
              {row.map((cell, x) => (
                <div 
                  key={`${x}-${y}`} 
                  className={`grid-cell ${cell.isActive ? 'active' : ''} ${
                    currentCell?.x === x && currentCell?.y === y ? 'selected' : ''
                  }`}
                  onClick={() => handleCellClick(x, y)}
                  onKeyDown={(e) => handleKeyPress(e, x, y)}
                  tabIndex={cell.isActive ? 0 : -1}
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
    </div>
  );
}

export default CrosswordGame;
