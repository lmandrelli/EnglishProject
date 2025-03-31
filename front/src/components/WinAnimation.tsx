import React, { useState, useEffect, useRef, useCallback } from 'react';
import './WinAnimation.css';

interface WinAnimationProps {
  onNextRound: () => void;
}

function WinAnimation({ onNextRound }: WinAnimationProps) {
  const [countdown, setCountdown] = useState(3);
  const [showMessage, setShowMessage] = useState(false);
  const messages = ["Awesome!", "Amazing!", "Fantastic!", "Great job!", "Brilliant!"];
  const [randomMessage] = useState(() => messages[Math.floor(Math.random() * messages.length)]);
  
  const hasTriggeredNextRoundRef = useRef(false);
  const onNextRoundRef = useRef(onNextRound);

  // Mettre à jour la référence chaque fois que onNextRound change
  useEffect(() => {
    onNextRoundRef.current = onNextRound;
  }, [onNextRound]);

  // Cette fonction est maintenant indépendante des rendus
  const triggerNextRound = useCallback(() => {
    if (!hasTriggeredNextRoundRef.current) {
      console.log('Executing onNextRound callback');
      hasTriggeredNextRoundRef.current = true;
      // Utiliser la référence pour appeler la fonction la plus récente
      onNextRoundRef.current();
    }
  }, []);

  useEffect(() => {
    console.log('WinAnimation mounted');
    setShowMessage(true);
    
    let messageTimer: ReturnType<typeof setTimeout>;
    let countdownTimer: ReturnType<typeof setInterval>;
    
    messageTimer = setTimeout(() => {
      console.log('Starting countdown');
      countdownTimer = setInterval(() => {
        setCountdown((prev) => {
          if (prev <= 1) {
            console.log('Countdown complete');
            clearInterval(countdownTimer);
            
            console.log('Triggering next round');
            // Déclencher le round suivant après un court délai
            setTimeout(triggerNextRound, 100);
            
            return 0;
          }
          return prev - 1;
        });
      }, 800);
    }, 100);
    
    // Ajouter un timer de secours pour s'assurer que onNextRound est appelé
    const backupTimer = setTimeout(() => {
      console.log('Backup timer triggered');
      triggerNextRound();
    }, 3000);
    
    return () => {
      console.log('Cleaning up timers');
      clearTimeout(messageTimer);
      clearInterval(countdownTimer);
      clearTimeout(backupTimer);
    };
  }, [triggerNextRound]);

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
