import React from 'react';
import './WinAnimation.css';

interface WinAnimationProps {
  onNextRound: () => void;
}

function WinAnimation({ onNextRound }: WinAnimationProps) {
  return (
    <div className="win-overlay">
      <div className="win-content">
        <h2>Victory!</h2>
        <div className="confetti-container">
          {[...Array(50)].map((_, i) => (
            <div key={i} className="confetti" style={{
              left: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              backgroundColor: `hsl(${Math.random() * 360}, 70%, 50%)`
            }} />
          ))}
        </div>
        <button className="next-round-btn" onClick={onNextRound}>
          Next Round
        </button>
      </div>
    </div>
  );
}

export default WinAnimation;
