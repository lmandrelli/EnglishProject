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
  const [selectedDish, setSelectedDish] = useState<number | null>(null);
  const [selectedCountry, setSelectedCountry] = useState<string | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(timeLimit);
  const [matchedPairs, setMatchedPairs] = useState<Set<number>>(new Set());
  const [shuffledDishes, setShuffledDishes] = useState<string[]>([]);
  const [uniqueCountries, setUniqueCountries] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [dishDescriptions, setDishDescriptions] = useState<Map<string, string>>(new Map());
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
      const data = await getCultureFoodOrigins(undefined, 5);
      setFoodOrigins(data);
      
      const descriptions = new Map<string, string>();
      data.forEach(item => {
        descriptions.set(item.dish_name, item.description);
      });
      setDishDescriptions(descriptions);
      
      // Using Fisher-Yates shuffle algorithm for better randomization
      const shuffle = <T,>(array: T[]): T[] => {
        const newArray = [...array];
        for (let i = newArray.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
        }
        return newArray;
      };

      // Shuffle dish names
      setShuffledDishes(shuffle(data.map(item => item.dish_name)));

      // Get unique countries and shuffle them
      const uniqueCountriesList = shuffle(
        Array.from(new Set(data.map(item => item.origin_country)))
      );
      setUniqueCountries(uniqueCountriesList);
      
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

  const handleSelection = (item: string | number, type: 'dish' | 'country') => {
    if (type === 'dish') {
      const dishIndex = item as number;
      if (matchedPairs.has(dishIndex)) return;
      setSelectedDish(dishIndex);
      setSelectedCountry(null);
    } else {
      const country = item as string;
      setSelectedCountry(country);
      setSelectedDish(null);
    }

    if ((type === 'dish' && selectedCountry) || (type === 'country' && selectedDish !== null)) {
      const dishIndex = type === 'dish' ? item as number : selectedDish as number;
      const country = type === 'country' ? item as string : selectedCountry as string;
      
      if (dishIndex >= foodOrigins.length) return;
      const dishItem = foodOrigins[dishIndex];
      const isMatch = dishItem.origin_country === country;
      
      if (isMatch) {
        const newMatchedPairs = new Set(matchedPairs);
        newMatchedPairs.add(dishIndex);
        setMatchedPairs(newMatchedPairs);
        // Get difficulty level from the matched item
        const matchedItem = foodOrigins[dishIndex];
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
        
        // Check if all dishes have been matched
        if (newMatchedPairs.size === foodOrigins.length) {
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

  // Helper function to get the count of a country's usage in matched pairs
  const getCountryMatchCount = (country: string): number => {
    return [...matchedPairs].reduce((count, index) => {
      return foodOrigins[index].origin_country === country ? count + 1 : count;
    }, 0);
  };

  // Helper function to get the total expected matches for a country
  const getCountryTotalCount = (country: string): number => {
    return foodOrigins.filter(food => food.origin_country === country).length;
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
          {foodOrigins.map((food, index) => (
            <div 
              key={`dish-${index}`}
              className={`food-card ${matchedPairs.has(index) ? 'matched' : ''} ${selectedDish === index ? 'selected' : ''}`}
              onClick={() => !matchedPairs.has(index) && handleSelection(index as number, 'dish')}
            >
              {food.dish_name}
              {matchedPairs.has(index) && (
                <div className="description-tooltip">
                  <p>{dishDescriptions.get(food.dish_name)}</p>
                  <p className="country-origin">Origin: {food.origin_country}</p>
                </div>
              )}
            </div>
          ))}
        </div>
        
        <div className="items-column countries-column">
          {uniqueCountries.map((country, index) => {
            const matchCount = getCountryMatchCount(country);
            const totalCount = getCountryTotalCount(country);
            return (
              <div 
                key={`country-${index}`}
                className={`word-card particle-card ${matchCount === totalCount ? 'matched' : ''} ${selectedCountry === country ? 'selected' : ''}`}
                onClick={() => matchCount < totalCount && handleSelection(country, 'country')}
              >
                <span className="particle-text">{country}</span>
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
       .particle-card {
          display: flex;
         justify-content: center;
         align-items: center;
         gap: 10px;
        }
        .particle-count {
          font-size: 0.8em;
          color:rgb(145, 145, 145);
        }
      `}</style>
    </div>
  );
}

export default FoodOriginsGame;
