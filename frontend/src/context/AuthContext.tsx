import { createContext, useContext, useState, useEffect, type ReactNode } from "react";
import { authApi, type RegisterPayload, type LoginPayload } from "../api/auth";

interface User {
  id: number;
  email: string;
  [key: string]: unknown;
}

interface AuthContextType {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (payload: LoginPayload) => Promise<void>;
  register: (payload: RegisterPayload) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("access_token")
  );
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadUser = async () => {
      if (token) {
        try {
          const userData = await authApi.getMe();
          setUser(userData);
        } catch {
          localStorage.removeItem("access_token");
          setToken(null);
          setUser(null);
        }
      }
      setIsLoading(false);
    };
    loadUser();
  }, [token]);

  const login = async (payload: LoginPayload) => {
    const response = await authApi.login(payload);
    localStorage.setItem("access_token", response.access_token);
    setToken(response.access_token);
  };

  const register = async (payload: RegisterPayload) => {
    const response = await authApi.register(payload);
    localStorage.setItem("access_token", response.access_token);
    setToken(response.access_token);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isAuthenticated: !!token && !!user,
        isLoading,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
