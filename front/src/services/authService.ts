import axios, { InternalAxiosRequestConfig, AxiosError } from 'axios';

const API_URL = 'http://localhost:8000/api/auth';

// Types pour l'authentification
export interface LoginRequest {
  username: string; // Email utilisé comme nom d'utilisateur pour OAuth2
  password: string;
}

export interface RegisterRequest {
  email: string;
  username: string;
  password: string;
}

export interface User {
  id: string;
  email: string;
  username: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

// Fonction pour s'inscrire
export const register = async (userData: RegisterRequest): Promise<User> => {
  const response = await axios.post<User>(`${API_URL}/register`, userData);
  return response.data;
};

// Fonction pour se connecter
export const login = async (credentials: LoginRequest): Promise<AuthResponse> => {
  const formData = new FormData();
  formData.append('username', credentials.username);
  formData.append('password', credentials.password);

  const response = await axios.post<AuthResponse>(`${API_URL}/token`, formData);
  if (response.data.access_token) {
    localStorage.setItem('token', response.data.access_token);
  }
  return response.data;
};

// Fonction pour récupérer l'utilisateur actuel
export const getCurrentUser = async (): Promise<User | null> => {
  const token = localStorage.getItem('token');
  if (!token) return null;

  try {
    const response = await axios.get<User>(`${API_URL}/me`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    return response.data;
  } catch (error) {
    logout();
    return null;
  }
};

// Fonction pour déconnecter l'utilisateur
export const logout = (): void => {
  localStorage.removeItem('token');
};

// Fonction pour vérifier si l'utilisateur est connecté
export const isAuthenticated = (): boolean => {
  return !!localStorage.getItem('token');
};

// Intercepteur pour ajouter le token à chaque requête
axios.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers = config.headers || {};
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error: AxiosError) => {
    return Promise.reject(error);
  }
);
