import { useEffect, useState } from 'react';
import { getCultureFoodOrigins, FoodOriginItem } from '../services/gameService';
import './CultureGames.css';

interface FoodOriginsGameProps {
  enemyScore: number;
  onWin: () => void;
  onLose: () => void;
}

function FoodOriginsGame({ enemyScore, onWin, onLose }: FoodOriginsGameProps) {
  const [currentScore, setCurrentScore] = useState(0);
  const [foodOrigins, setFoodOrigins] = useState<FoodOriginItem[]>([]);
  const [selectedDish, setSelectedDish] = useState<string | null>(null);
  const [selectedCountry, setSelectedCountry] = useState<string | null>(null);
  const [matchedPairs, setMatchedPairs] = useState<Set<string>>(new Set());
  const [attempts, setAttempts] = useState(0);
  const [shuffledDishes, setShuffledDishes] = useState<string[]>([]);
  const [shuffledCountries, setShuffledCountries] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [dishDescriptions, setDishDescriptions] = useState<Map<string, string>>(new Map());

  useEffect(() => {
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
        
        setLoading(false);
      } catch (err) {
        setError('Failed to load game data');
        setLoading(false);
        console.error(err);
      }
    };

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
        setCurrentScore(prevScore => prevScore + 200);
        
        if (newMatchedPairs.size === foodOrigins.length * 2) {
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
      
      setSelectedDish(null);
      setSelectedCountry(null);
    }
  };

  const getCountryForDish = (dishName: string): string => {
    const dish = foodOrigins.find(food => food.dish_name === dishName);
    return dish ? dish.origin_country : '';
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
        <h3>Match dishes with their countries of origin!</h3>
        <p>Click a dish and then its country of origin to make a match. You have {5 - attempts} attempts remaining.</p>
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