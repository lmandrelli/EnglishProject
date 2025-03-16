import { useEffect, useState } from 'react';
import './MainMenu.css';

function MainMenu() {
  const [particles, setParticles] = useState<Array<{ id: number, top: string, left: string, size: string, delay: string }>>([]);

  // Génère des particules en arrière-plan
  useEffect(() => {
    const particlesArray = [];
    for (let i = 0; i < 15; i++) {
      particlesArray.push({
        id: i,
        top: `${Math.random() * 100}%`,
        left: `${Math.random() * 100}%`,
        size: `${Math.random() * 10 + 2}px`,
        delay: `${Math.random() * 5}s`
      });
    }
    setParticles(particlesArray);
  }, []);

  const handleNewGame = () => {
    console.log('Commencer une nouvelle partie');
    // Logique pour démarrer une nouvelle partie
  };

  const handleLoadGame = () => {
    console.log('Charger une partie');
    // Logique pour charger une partie sauvegardée
  };

  return (
    <div className="main-menu">
      {/* Effets d'arrière-plan */}
      <div className="bg-wave"></div>
      <div className="bg-particles">
        {particles.map((particle) => (
          <div 
            key={particle.id} 
            className="particle" 
            style={{ 
              top: particle.top, 
              left: particle.left, 
              width: particle.size, 
              height: particle.size,
              animationDelay: particle.delay 
            }} 
          />
        ))}
      </div>

      {/* Contenu du menu */}
      <div className="menu-container">
        <div className="game-logo">
          <h1 className="game-title">Celestial Wordforge</h1>
        </div>

        <div className="menu-buttons">
          <button onClick={handleNewGame} className="button menu-button">
            Nouvelle Partie
          </button>
          <button onClick={handleLoadGame} className="button menu-button">
            Charger Partie
          </button>
        </div>
      </div>
    </div>
  );
}

export default MainMenu;