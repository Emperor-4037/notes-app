import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import "./Navbar.css";

export default function Navbar() {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-brand">
          <span className="navbar-icon">📝</span>
          <span className="navbar-logo">Notes</span>
        </Link>
        
        <div className="navbar-menu">
          {isAuthenticated ? (
            <div className="navbar-user">
              <span className="navbar-email">{user?.email}</span>
              <button onClick={handleLogout} className="btn-outline-danger btn-sm">
                Sign Out
              </button>
            </div>
          ) : (
            <div className="navbar-actions">
              <Link to="/login" className="btn-text">Sign In</Link>
              <Link to="/register" className="btn-primary btn-sm">Create Account</Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
