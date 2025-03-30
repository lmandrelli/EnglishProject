import { useEffect, useState } from 'react';
import { getTopScores, getUserScore } from '../services/leaderboardService';
import './Leaderboard.css';

interface LeaderboardEntry {
  id: string;
  user_id: string;
  username: string;
  score: number;
  created_at: string;
}

function Leaderboard() {
  const [topScores, setTopScores] = useState<LeaderboardEntry[]>([]);
  const [userScore, setUserScore] = useState<LeaderboardEntry | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchScores = async () => {
      setLoading(true);
      try {
        const [scores, personalScore] = await Promise.all([
          getTopScores(),
          getUserScore()
        ]);
        setTopScores(scores);
        setUserScore(personalScore);
      } catch (error) {
        console.error('Error fetching scores:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchScores();
  }, []);

  if (loading) {
    return <div className="leaderboard loading">Loading scores...</div>;
  }

  return (
    <div className="leaderboard">
      <h2>Top 10 Scores</h2>
      <div className="score-table">
        <div className="score-header">
          <div>Rank</div>
          <div>Player</div>
          <div>Score</div>
        </div>
        {topScores.map((score, index) => (
          <div 
            key={score.id} 
            className={`score-row ${score.user_id === userScore?.user_id ? 'current-user' : ''}`}
          >
            <div className="rank">{index + 1}</div>
            <div className="username">{score.username}</div>
            <div className="score">{score.score}</div>
          </div>
        ))}
        {topScores.length === 0 && (
          <div className="no-scores">No scores yet. Be the first!</div>
        )}
      </div>

      {userScore && !topScores.some(score => score.user_id === userScore.user_id) && (
        <div className="your-score">
          <h3>Your Best Score</h3>
          <div className="score-value">{userScore.score}</div>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
