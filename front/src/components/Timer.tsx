import React, { useEffect, useState } from 'react';
import './Timer.css';

interface TimerProps {
  duration: number; // Duration in seconds
  onTimeUp: () => void;
}

function Timer({ duration, onTimeUp }: TimerProps) {
  const [timeLeft, setTimeLeft] = useState(duration);
  const progress = (timeLeft / duration) * 100;

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft((prevTime) => {
        if (prevTime <= 1) {
          clearInterval(timer);
          onTimeUp();
          return 0;
        }
        return prevTime - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [duration, onTimeUp]);

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
