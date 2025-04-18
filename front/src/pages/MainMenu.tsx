import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Leaderboard from '../components/Leaderboard';
import './MainMenu.css';

function MainMenu() {
  const navigate = useNavigate();
  const { logout } = useAuth();
  const [particles, setParticles] = useState<Array<{ id: number, top: string, left: string, size: string, delay: string }>>([]);
  const [showLeaderboard, setShowLeaderboard] = useState(false);

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
    navigate('/Game');
  };

  const handleShowLeaderboard = () => {
    setShowLeaderboard(true);
  };

  const handleCloseLeaderboard = () => {
    setShowLeaderboard(false);
  };

  const handleDisconnect = () => {
    logout();
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
          <img src="/CelestialWordforge.png" alt="Celestial Wordforge" className="logo-image" />
          <h1 className="game-title">Celestial Wordforge</h1>
        </div>

        <div className="menu-buttons">
          <button onClick={handleNewGame} className="button menu-button">
            Nouvelle Partie
          </button>
          <button onClick={handleShowLeaderboard} className="button menu-button">
            Leaderboard
          </button>
          <button onClick={handleDisconnect} className="button menu-button menu-button-disconnect">
            Déconnexion
          </button>
        </div>
      </div>

      {showLeaderboard && (
        <div className="menu-overlay">
          <div className="menu-leaderboard">
            <button className="close-button" onClick={handleCloseLeaderboard}>×</button>
            <Leaderboard />
          </div>
        </div>
      )}
    </div>
  );
}

export default MainMenu;
