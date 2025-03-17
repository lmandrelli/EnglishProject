import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Login.css';

function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [particles, setParticles] = useState<Array<{ id: number, top: string, left: string, size: string, delay: string }>>([]);
  
  const navigate = useNavigate();
  const { login, register, isAuthenticated } = useAuth();

  // Rediriger si déjà connecté
  useEffect(() => {
    if (isAuthenticated) {
      navigate('/main-menu');
    }
  }, [isAuthenticated, navigate]);

  // Générer des particules en arrière-plan
  useEffect(() => {
    const particlesArray = [];
    for (let i = 0; i < 15; i++) {
      particlesArray.push({
        id: i,
        top: `${Math.random() * 100}%`,
        left: `${Math.random() * 100}%`,
        size: `${Math.random() * 10 + 2}px`,
        delay: `${Math.random() * 5}s`
      });
    }
    setParticles(particlesArray);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    try {
      if (isLogin) {
        await login({ username: email, password });
      } else {
        if (!username.trim()) {
          setError('Le nom d\'utilisateur est requis');
          return;
        }
        if (!email.includes('@')) {
          setError('Veuillez entrer une adresse email valide');
          return;
        }
        if (password.length < 6) {
          setError('Le mot de passe doit contenir au moins 6 caractères');
          return;
        }
        await register({ email, username, password });
      }
      navigate('/main-menu');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Une erreur est survenue, veuillez réessayer');
    }
  };

  const toggleForm = () => {
    setIsLogin(!isLogin);
    setError('');
  };

  return (
    <div className="login-container">
      {/* Effets d'arrière-plan */}
      <div className="login-particles">
        {particles.map((particle) => (
          <div 
            key={particle.id} 
            className="login-particle" 
            style={{ 
              top: particle.top, 
              left: particle.left, 
              width: particle.size, 
              height: particle.size,
              animationDelay: particle.delay 
            }} 
          />
        ))}
      </div>
      
      <div className="login-box">
        <div className="login-logo-container">
          <img src="/CelestialWordforge.png" alt="Celestial Wordforge" className="login-logo" />
          <h2 className="login-title">Celestial Wordforge</h2>
        </div>
        
        <form onSubmit={handleSubmit}>
          {!isLogin && (
            <div className="form-group">
              <label htmlFor="username">Nom d'utilisateur</label>
              <input
                type="text"
                id="username"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Entrez votre nom d'utilisateur"
                required
              />
            </div>
          )}
          
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              className="form-control"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Entrez votre email"
              required
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="password">Mot de passe</label>
            <input
              type="password"
              id="password"
              className="form-control"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Entrez votre mot de passe"
              required
            />
          </div>
          
          {error && <div className="error-message">{error}</div>}
          
          <button type="submit" className="menu-button">
            {isLogin ? 'Se connecter' : 'S\'inscrire'}
          </button>
        </form>
        
        <div className="toggle-form">
          {isLogin ? 'Pas encore de compte ?' : 'Déjà un compte ?'}
          <button onClick={toggleForm}>
            {isLogin ? 'S\'inscrire' : 'Se connecter'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
