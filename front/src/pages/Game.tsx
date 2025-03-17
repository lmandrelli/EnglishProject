import "./Game.css";
import { Home } from "lucide-react";
import { useNavigate } from "react-router-dom";

function Game() {
  const navigate = useNavigate();

  const handleHomeClick = () => {
    navigate("/");
  };

  return (
    <div className="game-container">
      <button className="home-button" onClick={handleHomeClick}>
        <Home size={24} />
      </button>
    </div>
  );
}

export default Game;
