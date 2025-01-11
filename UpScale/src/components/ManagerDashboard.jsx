/* eslint-disable no-unused-vars */
import React from 'react';
import { FaUser, FaProjectDiagram, FaChartLine, FaBookReader } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import './ManagerDashboard.css';

const ManagerDashboard = () => {
  const handleCardClick = (url) => {
    window.open(url, '_blank');
  };

  return (
    <div className="manager-dashboard">
      <nav className="manager-nav">
        <div className="nav-content">
          <div className="logo">Manager Dashboard</div>
          
          <div className="nav-menu">
            <Link to="/" className="nav-link">Home</Link>
            <Link to="/manager/profile" className="profile-section">
              <FaUser className="profile-icon" />
              <span className="profile-text">Profile</span>
            </Link>
          </div>
        </div>
      </nav>

      <main className="dashboard-content">
        <div className="welcome-section">
          <h1>Welcome to Manager Portal</h1>
          <p className="welcome-text">
            Access powerful tools and insights to effectively manage your projects and team. 
            Our platform provides comprehensive solutions for project management, performance tracking, 
            and professional development.
          </p>
          <div className="stats-container">
            <div className="stat-card">
              <h3>Active Projects</h3>
              <p className="stat-number">12</p>
            </div>
            <div className="stat-card">
              <h3>Team Members</h3>
              <p className="stat-number">24</p>
            </div>
            <div className="stat-card">
              <h3>Completion Rate</h3>
              <p className="stat-number">92%</p>
            </div>
          </div>
        </div>

        <div className="section-title">
          <h2>Management Tools</h2>
          <p>Access your essential management resources</p>
        </div>

        <div className="cards-container">
          {/* Manage Project Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://mainpy-egcunuzaym2lmtcswpqw4v.streamlit.app/')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3"
                alt="Project Management"
              />
            </div>
            <div className="card-content">
              <FaProjectDiagram className="card-icon" />
              <h3>Manage Projects</h3>
              <p>Oversee and manage all ongoing projects</p>
              <button className="card-button">View Projects</button>
            </div>
          </div>

          {/* Status Check Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://ashoksuthar2004.pythonanywhere.com/')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3"
                alt="Status Check"
              />
            </div>
            <div className="card-content">
              <FaChartLine className="card-icon" />
              <h3>Status Check</h3>
              <p>Monitor project progress and team performance</p>
              <button className="card-button">Check Status</button>
            </div>
          </div>

          {/* Project Course Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://ashoksuthar14.pythonanywhere.com/manager/dashboard')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3"
                alt="Project Courses"
              />
            </div>
            <div className="card-content">
              <FaBookReader className="card-icon" />
              <h3>Project Courses</h3>
              <p>Access training materials and courses</p>
              <button className="card-button">View Courses</button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default ManagerDashboard; 