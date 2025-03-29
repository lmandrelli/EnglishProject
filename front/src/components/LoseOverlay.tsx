import React from 'react';
import './LoseOverlay.css';

interface LoseOverlayProps {
  onReturnToMenu: () => void;
}

function LoseOverlay({ onReturnToMenu }: LoseOverlayProps) {
  return (
    <div className="lose-overlay">
      <div className="lose-content">
        <h2>Time's Up!</h2>
        <p>Better luck next time!</p>
        <button className="return-menu-btn" onClick={onReturnToMenu}>
          Return to Menu
        </button>
      </div>
    </div>
  );
}

export default LoseOverlay;
