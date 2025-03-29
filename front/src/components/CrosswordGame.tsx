import { useEffect, useState } from 'react';
import { getVocabularyCrossword } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
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
    case 1: return 10;
    case 2: return 25;
    case 3: return 50;
    default: return 10;
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
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);

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

    const wordArray = Array.from({ length: word.word.length }, (_, i) => {
      const x = word.direction === 'across' ? word.startX + i : word.startX;
      const y = word.direction === 'down' ? word.startY + i : word.startY;
      return userInputs[`${x},${y}`] || '';
    });

    // Return early if any letter is missing
    if (wordArray.some(letter => letter === '')) {
      return false;
    }

    // All letters are filled, proceed with validation
    {
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

    if (enteredWord.toUpperCase() === word.word.toUpperCase()) {
      // Word is correct! We'll handle this in a separate function
      setTimeout(() => validateCorrectWord(word, userInputs), 10);
      return true;
    }
    return false;
  };

  const validateCorrectWord = (word: Word, inputs: { [key: string]: string }) => {
    const newCompleted = new Set(completedWords);
    newCompleted.add(word.word);
    setCompletedWords(newCompleted);
    
    const points = word.word.length * getPointsPerLetter(word.difficulty);
    const newScore = currentScore + points;
    setCurrentScore(newScore);

    const newGrid = [...grid];
    for (let i = 0; i < word.word.length; i++) {
      const x = word.direction === 'across' ? word.startX + i : word.startX;
      const y = word.direction === 'down' ? word.startY + i : word.startY;
      newGrid[y][x].letter = word.word[i].toUpperCase(); // Assurer que les lettres sont en majuscules
    }
    setGrid(newGrid);

    setSelectedWord(null);
    setCurrentCell(null);
    setCurrentDirection(null);

    if (newCompleted.size === words.length) {
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
  };

  const resetIncorrectWord = (word: Word) => {
    // Reset word cells and mark them red
    for (let i = 0; i < word.word.length; i++) {
      const x = word.direction === 'across' ? word.startX + i : word.startX;
      const y = word.direction === 'down' ? word.startY + i : word.startY;
      const cellKey = `${x},${y}`;
      
      // Reset the inputs
      setUserInputs(prev => {
        const newInputs = { ...prev };
        delete newInputs[cellKey];
        return newInputs;
      });

      // Highlight cells as incorrect
      const cell = document.querySelector(`[data-position="${x},${y}"]`) as HTMLElement;
      if (cell) {
        cell.classList.add('incorrect');
        setTimeout(() => cell.classList.remove('incorrect'), 1000);
      }
    }
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
    // Vérifier si la cellule appartient au mot sélectionné, même si elle fait partie d'un autre mot déjà complété
    const isPartOfSelectedWord = selectedWord && (
      (selectedWord.direction === 'across' && 
        y === selectedWord.startY && 
        x >= selectedWord.startX && 
        x < selectedWord.startX + selectedWord.word.length) ||
      (selectedWord.direction === 'down' && 
        x === selectedWord.startX && 
        y >= selectedWord.startY && 
        y < selectedWord.startY + selectedWord.word.length)
    );

    // Empêcher la saisie seulement si :
    // - la cellule n'est pas active, ou
    // - le mot est déjà complété, ou
    // - aucun mot n'est sélectionné, ou 
    // - la cellule n'appartient pas au mot sélectionné
    if (!grid[y][x].isActive || !selectedWord || completedWords.has(selectedWord.word) || !isPartOfSelectedWord) return;
    
    if (/^[a-zA-Z]$/.test(e.key)) {
      const letter = e.key.toUpperCase(); // Toujours mettre en majuscule
      const cellKey = `${x},${y}`;
      
      // Mise à jour directe de la lettre dans un objet temporaire avant validation
      const updatedInputs = { ...userInputs, [cellKey]: letter };
      
      // Appliquer la mise à jour à l'état
      setUserInputs(updatedInputs);
      
      // Vérifier si le mot est complet après chaque saisie
      if (selectedWord) {
        const wordArray = Array.from({ length: selectedWord.word.length }, (_, i) => {
          const letterX = selectedWord.direction === 'across' ? selectedWord.startX + i : selectedWord.startX;
          const letterY = selectedWord.direction === 'down' ? selectedWord.startY + i : selectedWord.startY;
          return updatedInputs[`${letterX},${letterY}`] || '';
        });
        
        const isComplete = wordArray.every(l => l !== '');
        
        if (isComplete) {
          // Validation immédiate en utilisant les données mises à jour
          const enteredWord = wordArray.join('');
          if (enteredWord.toUpperCase() === selectedWord.word.toUpperCase()) {
            // Mot correct - valider immédiatement
            const newCompleted = new Set(completedWords);
            newCompleted.add(selectedWord.word);
            setCompletedWords(newCompleted);
            
            const points = selectedWord.word.length * getPointsPerLetter(selectedWord.difficulty);
            const newScore = currentScore + points;
            setCurrentScore(newScore);
            
            const newGrid = [...grid];
            for (let i = 0; i < selectedWord.word.length; i++) {
              const cellX = selectedWord.direction === 'across' ? selectedWord.startX + i : selectedWord.startX;
              const cellY = selectedWord.direction === 'down' ? selectedWord.startY + i : selectedWord.startY;
              newGrid[cellY][cellX].letter = selectedWord.word[i].toUpperCase(); // Assurer que les lettres sont en majuscules
            }
            setGrid(newGrid);
            
            setSelectedWord(null);
            setCurrentCell(null);
            setCurrentDirection(null);
            
            // Vérifier si tous les mots sont complétés
            if (newCompleted.size === words.length) {
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
            return; // Sortir de la fonction après avoir validé le mot
          } else {
            // Mot incorrect - réinitialiser
            for (let i = 0; i < selectedWord.word.length; i++) {
              const resetX = selectedWord.direction === 'across' ? selectedWord.startX + i : selectedWord.startX;
              const resetY = selectedWord.direction === 'down' ? selectedWord.startY + i : selectedWord.startY;
              const resetKey = `${resetX},${resetY}`;
              
              // Effacer les saisies utilisateur (sauf la touche qui vient d'être pressée)
              if (resetKey !== cellKey) {
                setUserInputs(prev => {
                  const newInputs = { ...prev };
                  delete newInputs[resetKey];
                  return newInputs;
                });
              }
              
              // Animer les cellules incorrectes
              const cell = document.querySelector(`[data-position="${resetX},${resetY}"]`) as HTMLElement;
              if (cell) {
                cell.classList.add('incorrect');
                setTimeout(() => cell.classList.remove('incorrect'), 1000);
              }
            }
          }
        }
      }
      
      // Gestion de la navigation entre les cellules (déplacement à la suivante après la saisie)
      if (currentDirection) {
        // Passer à la cellule suivante non-validée
        let nextX = x;
        let nextY = y;
        let found = false;
        
        // Chercher la prochaine cellule non-validée dans la direction actuelle
        while (!found) {
          if (currentDirection === 'across') {
            nextX += 1;
          } else {
            nextY += 1;
          }
          
          // Vérifier si la position est encore dans la grille et fait partie du mot
          const isWithinGrid = nextX < grid[0].length && nextY < grid.length;
          const isPartOfSelectedWord = selectedWord && (
            (currentDirection === 'across' && 
             nextY === selectedWord.startY && 
             nextX >= selectedWord.startX && 
             nextX < selectedWord.startX + selectedWord.word.length) ||
            (currentDirection === 'down' && 
             nextX === selectedWord.startX && 
             nextY >= selectedWord.startY && 
             nextY < selectedWord.startY + selectedWord.word.length)
          );
          
          if (!isWithinGrid || !isPartOfSelectedWord) {
            // Si on a dépassé les limites du mot ou de la grille, rester sur la cellule actuelle
            nextX = x;
            nextY = y;
            found = true;
          } else if (grid[nextY][nextX].isActive) {
            // On a trouvé une cellule, qu'elle soit déjà validée ou non
            found = true;
          }
        }
        
        setCurrentCell({ x: nextX, y: nextY });
      }
    } else if (e.key === 'Backspace' || e.key === 'Delete') {
      // Effacer le contenu de la cellule actuelle
      const cellKey = `${x},${y}`;
      
      if (userInputs[cellKey]) {
        // Si la cellule actuelle contient une lettre, l'effacer
        setUserInputs(prev => {
          const newInputs = { ...prev };
          delete newInputs[cellKey];
          return newInputs;
        });
      } else if (currentDirection) {
        // Si la cellule est vide, aller à la cellule précédente non-validée
        let prevX = x;
        let prevY = y;
        let found = false;
        
        // Chercher la cellule précédente non-validée
        while (!found) {
          if (currentDirection === 'across') {
            prevX -= 1;
          } else {
            prevY -= 1;
          }
          
          // Vérifier si on est encore dans le mot
          const isWithinWord = (
            (currentDirection === 'across' && 
             prevY === selectedWord?.startY && 
             prevX >= selectedWord?.startX) ||
            (currentDirection === 'down' && 
             prevX === selectedWord?.startX && 
             prevY >= selectedWord?.startY)
          );
          
          if (prevX < 0 || prevY < 0 || !isWithinWord) {
            // Si on sort du mot ou de la grille, rester sur la cellule actuelle
            prevX = x;
            prevY = y;
            found = true;
          } else if (grid[prevY] && grid[prevY][prevX] && 
                     grid[prevY][prevX].isActive && 
                     !isCompletedCell(prevX, prevY)) {
            // On a trouvé une cellule valide non complétée
            found = true;
          }
        }
        
        if (prevX !== x || prevY !== y) {
          // Effacer le contenu de la cellule précédente
          const prevCellKey = `${prevX},${prevY}`;
          setUserInputs(prev => {
            const newInputs = { ...prev };
            delete newInputs[prevCellKey];
            return newInputs;
          });
          
          // Déplacer le focus à la cellule précédente
          setCurrentCell({ x: prevX, y: prevY });
        }
      }
    } else if (e.key === 'Enter' || e.key === 'Return') {
      // Corriger la dernière entrée
      if (selectedWord && currentDirection) {
        // Calculer les coordonnées de la dernière cellule remplie
        let lastFilledX = x;
        let lastFilledY = y;
        
        if (currentDirection === 'across') {
          for (let i = 1; i <= x - selectedWord.startX; i++) {
            const checkX = x - i;
            const checkY = y;
            const checkKey = `${checkX},${checkY}`;
            
            if (!userInputs[checkKey]) break;
            lastFilledX = checkX;
          }
        } else { // down
          for (let i = 1; i <= y - selectedWord.startY; i++) {
            const checkX = x;
            const checkY = y - i;
            const checkKey = `${checkX},${checkY}`;
            
            if (!userInputs[checkKey]) break;
            lastFilledY = checkY;
          }
        }
        
        // Effacer le contenu de la dernière cellule remplie
        const lastCellKey = `${lastFilledX},${lastFilledY}`;
        if (userInputs[lastCellKey]) {
          setUserInputs(prev => {
            const newInputs = { ...prev };
            delete newInputs[lastCellKey];
            return newInputs;
          });
          
          // Déplacer le focus à cette cellule
          setCurrentCell({ x: lastFilledX, y: lastFilledY });
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
    // Vérifier le score avant d'afficher le menu approprié
    if (currentScore >= enemyScore) {
      // Si le score est suffisant, afficher l'animation de victoire
      const gridElement = document.querySelector('.grid') as HTMLElement;
      if (gridElement) {
        gridElement.classList.add('winning-grid');
        setTimeout(() => {
          setShowWinAnimation(true);
        }, 1000);
      }
    } else {
      // Sinon, afficher le menu de défaite
      setShowLoseOverlay(true);
    }
  };

  const handleReturnToMenu = () => {
    setShowLoseOverlay(false);
    onLose();
  };

  return (
    <div className="crossword-game">
      {showWinAnimation && <WinAnimation onNextRound={handleNextRound} />}
      {showLoseOverlay && <LoseOverlay onReturnToMenu={handleReturnToMenu} />}
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
                    tabIndex={cell.isActive && (currentCell?.x === x && currentCell?.y === y ? 0 : -1)}
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
