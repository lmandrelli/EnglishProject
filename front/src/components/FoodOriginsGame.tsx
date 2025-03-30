import { useEffect, useState } from 'react';
import { getCultureFoodOrigins, FoodOriginItem } from '../services/gameService';
import Timer from './Timer';
import WinAnimation from './WinAnimation';
import LoseOverlay from './LoseOverlay';
import './CultureGames.css';

interface FoodOriginsGameProps {
  enemyScore: number;
  onWin: (score: number) => void;
  onLose: (score: number) => void;
  timeLimit?: number; // Temps limite en secondes (par défaut: 120)
  currentScore?: number;
}

function FoodOriginsGame({ enemyScore, onWin, onLose, timeLimit = 120 }: FoodOriginsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [foodOrigins, setFoodOrigins] = useState<FoodOriginItem[]>([]);
  const [selectedDish, setSelectedDish] = useState<string | null>(null);
  const [selectedCountry, setSelectedCountry] = useState<string | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [matchedPairs, setMatchedPairs] = useState<Set<string>>(new Set());
  const [shuffledDishes, setShuffledDishes] = useState<string[]>([]);
  const [shuffledCountries, setShuffledCountries] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [dishDescriptions, setDishDescriptions] = useState<Map<string, string>>(new Map());
  const [showWinAnimation, setShowWinAnimation] = useState(false);
  const [showLoseOverlay, setShowLoseOverlay] = useState(false);
  const [hasWon, setHasWon] = useState(false);

  const handleVictory = () => {
    if (!hasWon) {
      setHasWon(true);
      setShowWinAnimation(true);
    }
  };

  const fetchData = async () => {
    try {
      setLoading(true);
      const data = await getCultureFoodOrigins(undefined, 5);
      setFoodOrigins(data);
      
      const descriptions = new Map<string, string>();
      data.forEach(item => {
        descriptions.set(item.dish_name, item.description);
      });
      setDishDescriptions(descriptions);
      
      setShuffledDishes(data.map(item => item.dish_name).sort(() => Math.random() - 0.5));
      setShuffledCountries(data.map(item => item.origin_country).sort(() => Math.random() - 0.5));
      
      setMatchedPairs(new Set());
      setSelectedDish(null);
      setSelectedCountry(null);
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

  const handleSelection = (item: string, type: 'dish' | 'country') => {
    if (matchedPairs.has(item)) return;
    if (type === 'dish') {
      setSelectedDish(item);
      setSelectedCountry(null);
    } else {
      setSelectedCountry(item);
      setSelectedDish(null);
    }
    if ((type === 'dish' && selectedCountry) || (type === 'country' && selectedDish)) {
      const dish = type === 'dish' ? item : selectedDish;
      const country = type === 'country' ? item : selectedCountry;
      
      const isMatch = foodOrigins.some(
        food => food.dish_name === dish && food.origin_country === country
      );
      if (isMatch) {
        const newMatchedPairs = new Set(matchedPairs);
        newMatchedPairs.add(dish as string);
        newMatchedPairs.add(country as string);
        setMatchedPairs(newMatchedPairs);
        // Find the matched item to get its difficulty level
        const matchedItem = foodOrigins.find(
          food => food.dish_name === dish && food.origin_country === country
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
        
        // Vérifier si tous les plats ont été associés
        if (newMatchedPairs.size === foodOrigins.length * 2) {
          // Vérifier si le score est suffisant pour gagner
          if (currentScore + difficultyScore > enemyScore) {
            setTimeout(handleVictory, 500);
          } else {
            // Recharger le jeu avec un nouveau set de plats sans réinitialiser le timer
            fetchData();
          }
        }
      } else {
        setCurrentScore(prevScore => Math.max(0, prevScore - 50));
      }
      
      setSelectedDish(null);
      setSelectedCountry(null);
    }
  };

  const getCountryForDish = (dishName: string): string => {
    const dish = foodOrigins.find(food => food.dish_name === dishName);
    return dish ? dish.origin_country : '';
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
        <h3>Match dishes with their countries of origin!</h3>
        <p>Click a dish and then its country of origin to make a match.</p>
      </div>
      
      <div className="food-origins-game">
        <div className="column-header dishes">
          <h3>Dishes</h3>
        </div>
        
        <div className="column-header countries">
          <h3>Countries</h3>
        </div>
        
        <div className="items-column dishes-column">
          {shuffledDishes.map((dish, index) => (
            <div 
              key={`dish-${index}`}
              className={`food-card ${matchedPairs.has(dish) ? 'matched' : ''} ${selectedDish === dish ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(dish) && handleSelection(dish, 'dish')}
            >
              {dish}
              {matchedPairs.has(dish) && (
                <div className="description-tooltip">
                  <p>{dishDescriptions.get(dish)}</p>
                  <p className="country-origin">Origin: {getCountryForDish(dish)}</p>
                </div>
              )}
            </div>
          ))}
        </div>
        
        <div className="items-column countries-column">
          {shuffledCountries.map((country, index) => (
            <div 
              key={`country-${index}`}
              className={`food-card ${matchedPairs.has(country) ? 'matched' : ''} ${selectedCountry === country ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(country) && handleSelection(country, 'country')}
            >
              {country}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default FoodOriginsGame;
