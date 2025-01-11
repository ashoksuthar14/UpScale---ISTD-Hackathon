/* eslint-disable no-unused-vars */
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Dashboard.css';

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <nav className="navbar">
        <div className="navbar-content">
          <div className="logo">AI Learning Platform</div>
          <div className="nav-links">
            <Link to="/" className="nav-link">Home</Link>
            <Link to="/manager" className="nav-link">Manager</Link>
            <Link to="/employee" className="nav-link">Employee</Link>
            <a href="https://ashoksuthar.pythonanywhere.com/" className="nav-link" target="_blank" rel="noopener noreferrer">Guidance</a>

            <Link to="/login" className="nav-link login-link">Login</Link>
          </div>
        </div>
      </nav>

      <main className="main-content">
        <div className="hero-section">
          <div className="hero-content">
            <h1>Welcome to AI Learning Platform</h1>
            <p>Empower your journey in Artificial Intelligence and Machine Learning</p>
            <Link to="/login" className="get-started-btn">Get Started Now</Link>
          </div>
          <div className="hero-image">
            <img 
              src="https://images.unsplash.com/photo-1677442136019-21780ecad995" 
              alt="AI Learning"
            />
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;