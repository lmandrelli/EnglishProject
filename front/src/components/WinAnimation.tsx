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
  const [hasTriggeredNextRound, setHasTriggeredNextRound] = useState(false);

  useEffect(() => {
    console.log('WinAnimation mounted');
    setShowMessage(true);
    
    let messageTimer: ReturnType<typeof setTimeout>;
    let countdownTimer: ReturnType<typeof setInterval>;
    let nextRoundTimer: ReturnType<typeof setTimeout>;

    messageTimer = setTimeout(() => {
      console.log('Starting countdown');
      countdownTimer = setInterval(() => {
        setCountdown((prev) => {
          if (prev <= 1) {
            console.log('Countdown complete');
            clearInterval(countdownTimer);
            if (!hasTriggeredNextRound) {
              console.log('Triggering next round');
              setHasTriggeredNextRound(true);
              nextRoundTimer = setTimeout(() => {
                console.log('Calling onNextRound');
                onNextRound();
              }, 100);
            }
            return 0;
          }
          return prev - 1;
        });
      }, 800);
    }, 100);
    
    return () => {
      console.log('Cleaning up timers');
      clearTimeout(messageTimer);
      clearInterval(countdownTimer);
      clearTimeout(nextRoundTimer);
    };
  }, [onNextRound, hasTriggeredNextRound]);

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
