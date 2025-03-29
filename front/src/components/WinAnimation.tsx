import React, { useState, useEffect } from 'react';
import './WinAnimation.css';

interface WinAnimationProps {
  onNextRound: () => void;
}

function WinAnimation({ onNextRound }: WinAnimationProps) {
  const [countdown, setCountdown] = useState(3);
  const [showMessage, setShowMessage] = useState(false);
  const messages = ["Awesome!", "Amazing!", "Fantastic!", "Great job!", "Brilliant!"];
  const [randomMessage] = useState(() => messages[Math.floor(Math.random() * messages.length)]);

  // Afficher le message de victoire immédiatement
  useEffect(() => {
    setShowMessage(true);
    
    // Démarrer le compte à rebours après 1.5 secondes
    const messageTimer = setTimeout(() => {
      const timer = setInterval(() => {
        setCountdown((prev) => {
          if (prev <= 1) {
            clearInterval(timer);
            // Lancement automatique du prochain round après la fin du compte à rebours
            setTimeout(onNextRound, 100);
            return 0;
          }
          return prev - 1;
        });
      }, 800);
      
      return () => clearInterval(timer);
    }, 100);
    
    return () => clearTimeout(messageTimer);
  }, [onNextRound]);

  return (
    <div className="win-overlay">
      
      <div className="win-content">
        {showMessage && (
          <div className="victory-message">
            <h2 className="victory-text">{randomMessage}</h2>
          </div>
        )}
        
        {countdown > 0 ? (
          <div className="next-round-container">
            <h3>Next Round In</h3>
            <div className="countdown">{countdown}</div>
          </div>
        ) : (
          <div className="ready-message">Ready!</div>
        )}
      </div>
    </div>
  );
}

export default WinAnimation;
