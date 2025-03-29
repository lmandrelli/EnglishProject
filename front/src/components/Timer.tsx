import React, { useEffect, useState } from 'react';
import './Timer.css';

interface TimerProps {
  duration: number; // Duration in seconds
  onTimeUp: () => void;
  initialTime?: number; // Optional initial time value
  onTimeChange?: (time: number) => void; // Callback for time updates
}

function Timer({ duration, onTimeUp, initialTime, onTimeChange }: TimerProps) {
  const [timeLeft, setTimeLeft] = useState(initialTime ?? duration);
  const progress = (timeLeft / duration) * 100;

  useEffect(() => {
    if (onTimeChange) {
      onTimeChange(timeLeft);
    }
    const timer = setInterval(() => {
      setTimeLeft((prevTime) => {
        const newTime = prevTime <= 1 ? 0 : prevTime - 1;
        if (onTimeChange) {
          onTimeChange(newTime);
        }
        if (newTime === 0) {
          clearInterval(timer);
          onTimeUp();
        }
        return newTime;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [duration, onTimeUp, onTimeChange]);

  const formatTime = (seconds: number) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  };

  return (
    <div className="timer">
      <div className="timer-label">{formatTime(timeLeft)}</div>
      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ 
            width: `${progress}%`,
            backgroundColor: `hsl(${progress}, 70%, 50%)`
          }} 
        />
      </div>
    </div>
  );
}

export default Timer;
