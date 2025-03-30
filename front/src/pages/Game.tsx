import { useEffect, useState } from "react";
import "./Game.css";
import { Home } from "lucide-react";
import { useNavigate } from "react-router-dom";
import CrosswordGame from "../components/CrosswordGame";
import ErrorDetectionGame from "../components/ErrorDetectionGame";
import RegionalVariantsGame from "../components/RegionalVariantsGame";
import FoodOriginsGame from "../components/FoodOriginsGame";
import IdiomsGame from "../components/IdiomsGame";
import SynonymMatchGame from "../components/SynonymMatchGame";
import PhrasalVerbGame from "../components/PhrasalVerbGame";
import WordCompletionGame from "../components/WordCompletionGame";
import VerbFormsGame from "../components/VerbFormsGame";

type GameMode = {
  id: string;
  name: string;
  description: string;
};

const GAME_MODES = {
  p3: [
    { id: 'word_puzzle', name: 'Word Puzzle', description: 'Solve crossword challenges' },
    { id: 'word_completion', name: 'Word Completion', description: 'Fill in the missing words' },
    { id: 'word_matching', name: 'Word Matching', description: 'Match words with their synonyms' }
  ],
  p4: [
    { id: 'error_detection', name: 'Error Detection', description: 'Find the wrong word' },
    { id: 'verb_forms', name: 'Verb Forms', description: 'Practice verb conjugations' },
    { id: 'verb_combinations', name: 'Verb Combinations', description: 'Master phrasal verbs' }
  ],
  p5: [
    { id: 'regional_variants', name: 'Regional Variants', description: 'Learn UK/US differences' },
    { id: 'cultural_origins', name: 'Cultural Origins', description: 'Identify food nationalities' },
    { id: 'expression_mastery', name: 'Expression Mastery', description: 'Find the correct idiom' }
  ]
};

interface Enemy {
  type: 'p3' | 'p4' | 'p5' | 'boss';
  image: string;
  score: number;
  id: string;
  gameModes: GameMode[];
}

interface GameState {
  mode: GameMode | null;
  inProgress: boolean;
}

function Game() {
  const navigate = useNavigate();
  const [currentRound, setCurrentRound] = useState(1);
  const [enemies, setEnemies] = useState<Enemy[]>([]);
  const [selectedEnemy, setSelectedEnemy] = useState<Enemy | null>(null);
  const [gameState, setGameState] = useState<GameState>({ mode: null, inProgress: false });

  // Get random game modes for an enemy type
  const getGameModes = (type: 'p3' | 'p4' | 'p5' | 'boss'): GameMode[] => {
    if (type === 'boss') {
      // For boss, randomly select 1-3 modes from all available modes
      const allModes = [...GAME_MODES.p3, ...GAME_MODES.p4, ...GAME_MODES.p5];
      const numModes = Math.floor(Math.random() * 3) + 1; // 1 to 3 modes
      const shuffled = allModes.sort(() => 0.5 - Math.random());
      return shuffled.slice(0, numModes);
    }
    
    // For regular enemies, return all 3 modes for their type
    return GAME_MODES[type];
  };

  // Get random image for specific enemy type
  const getRandomImage = (type: 'p3' | 'p4' | 'p5' | 'boss'): string => {
    if (type === 'boss') {
      const bossImages = ['boss1.png.jpeg', 'boss2.png.jpeg', 'boss3.png.jpeg'];
      return bossImages[Math.floor(Math.random() * bossImages.length)];
    }
    
    const images = [1, 2, 3].map(num => `${type}_${num}.jpeg`);
    return images[Math.floor(Math.random() * images.length)];
  };

  // Generate score based on round number
  const generateScore = (roundNum: number, isBoss: boolean, baseScore?: number): number => {
    const cycleNum = Math.floor((roundNum - 1) / 3); // 0, 1, 2, etc. for each cycle
    let score: number;

    if (isBoss) {
      // Boss score progression: 500, 1000, 5000, 10000, etc.
      score = cycleNum === 0 ? 500 : 450 * (cycleNum + 1);
    } else {
      // Regular enemies score
      const baseRoundScore = cycleNum === 0 ? 200 : 300 * cycleNum;
      
      if (baseScore) {
        // Generate score within ±50 of base score for consistent round scores
        score = baseScore + Math.floor(Math.random() * 100) - 50;
      } else {
        // First enemy in round, generate base score
        score = baseRoundScore + Math.floor(Math.random() * 100);
      }
    }

    return Math.max(100, score); // Ensure minimum score of 100
  };

  // Set up enemies for the round
  useEffect(() => {
    let roundEnemies: Enemy[] = [];
    console.log(`Setting up round ${currentRound}`);
    const isBossRound = currentRound % 3 === 0;
    console.log(`Is boss round: ${isBossRound}`);
    
    if (isBossRound) {
      // Boss round
      roundEnemies = [{
        type: 'boss',
        image: getRandomImage('boss'),
        score: generateScore(currentRound, true),
        id: `boss-${currentRound}`,
        gameModes: getGameModes('boss')
      }];
    } else {
      // Regular round with three enemies
      const types: ('p3' | 'p4' | 'p5')[] = ['p3', 'p4', 'p5'];
      const baseScore = generateScore(currentRound, false);
      roundEnemies = types.map(type => ({
        type,
        image: getRandomImage(type),
        score: generateScore(currentRound, false, baseScore),
        id: `${type}-${currentRound}-${Math.random()}`,
        gameModes: getGameModes(type)
      }));
    }
    
    setEnemies(roundEnemies);
  }, [currentRound]);

  const handleEnemyClick = (enemy: Enemy) => {
    if (!selectedEnemy) {
      const isBossRound = currentRound % 3 === 0;
      
      if (isBossRound) {
        console.log('boss -> all');
      } else {
        switch (enemy.type) {
          case 'p3':
            console.log('p3 -> Vocab');
            break;
          case 'p4':
            console.log('p4 -> Grammar');
            break;
          case 'p5':
            console.log('p5 -> Culture');
            break;
        }
      }
      
      setSelectedEnemy(enemy);
    }
  };

  const handleHomeClick = () => {
    navigate("/");
  };

  const handleNextRound = () => {
    setSelectedEnemy(null);
    setGameState({ mode: null, inProgress: false });
    setCurrentRound(prev => prev + 1);
  };

  const handleModeSelect = (mode: GameMode) => {
    setGameState({ mode, inProgress: true });
  };

  const handleGameWin = () => {
    handleNextRound();
  };

  const handleGameLose = () => {
    navigate("/main-menu");
  };

  return (
    <div className="game-container">
      <button className="home-button" onClick={handleHomeClick}>
        <Home size={24} />
      </button>

      {selectedEnemy && (
        <div className="battle-area">
          <div className="selected-enemy">
            <div className="enemy-card">
              <div className="score">{selectedEnemy.score}</div>
              <img src={`/${selectedEnemy.image}`} alt={`Enemy ${selectedEnemy.type}`} />
            </div>
          </div>

          {!gameState.inProgress && (
            <div className="game-modes">
              {selectedEnemy.gameModes.map(mode => (
                <div 
                  key={mode.id} 
                  className="game-mode"
                  onClick={() => handleModeSelect(mode)}
                >
                  <h3>{mode.name}</h3>
                  <p>{mode.description}</p>
                </div>
              ))}
            </div>
          )}

          {gameState.mode?.id === 'word_puzzle' && (
            <div className="game-container">
              <CrosswordGame
                wordCount={5}
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'regional_variants' && (
            <div className="game-container">
              <RegionalVariantsGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'cultural_origins' && (
            <div className="game-container">
              <FoodOriginsGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'expression_mastery' && (
            <div className="game-container">
              <IdiomsGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'word_matching' && (
            <div className="game-container">
              <SynonymMatchGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'verb_combinations' && (
            <div className="game-container">
              <PhrasalVerbGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'word_completion' && (
            <div className="game-container">
              <WordCompletionGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'error_detection' && (
            <div className="game-container">
              <ErrorDetectionGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}

          {gameState.mode?.id === 'verb_forms' && (
            <div className="game-container">
              <VerbFormsGame
                enemyScore={selectedEnemy.score}
                onWin={handleGameWin}
                onLose={handleGameLose}
                timeLimit={60}
              />
            </div>
          )}
        </div>
      )}
      {!selectedEnemy && (
        <div className="enemies-container">
          {enemies.map((enemy) => (
            <div 
              key={enemy.id} 
              className="enemy-card"
              onClick={() => handleEnemyClick(enemy)}
            >
              <div className="score">{enemy.score}</div>
              <img src={`/${enemy.image}`} alt={`Enemy ${enemy.type}`} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Game;
