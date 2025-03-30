import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

interface LeaderboardEntry {
  id: string;
  user_id: string;
  username: string;
  score: number;
  created_at: string;
}

export const submitScore = async (score: number): Promise<boolean> => {
  try {
    const response = await axios.post(
      `${API_URL}/api/leaderboard/submit`,
      { score },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      }
    );
    return response.data.success;
  } catch (error) {
    console.error('Error submitting score:', error);
    return false;
  }
};

export const getTopScores = async (): Promise<LeaderboardEntry[]> => {
  try {
    const response = await axios.get(`${API_URL}/api/leaderboard/top`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data.scores;
  } catch (error) {
    console.error('Error fetching top scores:', error);
    return [];
  }
};

export const getUserScore = async (): Promise<LeaderboardEntry | null> => {
  try {
    const response = await axios.get(`${API_URL}/api/leaderboard/user`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response?.status === 404) {
      // No score exists yet for this user
      return null;
    }
    console.error('Error fetching user score:', error);
    return null;
  }
};
