import { Routes, Route, Navigate } from 'react-router-dom';
import MainMenu from './pages/MainMenu';
import Login from './pages/Login';
import Game from './pages/Game';
import { PrivateRoute } from './components/PrivateRoute';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/main-menu"
          element={
            <PrivateRoute>
              <MainMenu />
            </PrivateRoute>
          }
        />
        <Route
         path="/game"
         element={
           <PrivateRoute>
              <Game />
            </PrivateRoute>
          }
        />
        <Route path="/" element={<Navigate to="/login" replace />} />
      </Routes>
    </div>
  );
}

export default App;
