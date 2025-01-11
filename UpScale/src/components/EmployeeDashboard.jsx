/* eslint-disable no-unused-vars */
import React from 'react';
import { FaRoad, FaYoutube, FaQuestionCircle, FaBook, FaUser } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import './EmployeeDashboard.css';

const EmployeeDashboard = () => {
  const handleCardClick = (url) => {
    window.open(url, '_blank');
  };

  return (
    <div className="employee-dashboard">
      <nav className="employee-nav">
        <div className="nav-content">
          <div className="logo">Employee Portal</div>
          <div className="nav-menu">
            <a href="/" className="nav-link">Home</a>
            
            
            <Link to="/employee/profile" className="profile-section">
              <FaUser className="profile-icon" />
              <span>Profile</span>
            </Link>
          </div>
        </div>
      </nav>

      <main className="dashboard-content">
        <div className="welcome-section">
          <h1>Welcome to Learning Hub</h1>
          <p className="welcome-text">
            Embark on your learning journey with our comprehensive resources and tools.
            Enhance your skills and advance your career with our curated content.
          </p>
          <div className="stats-container">
            <div className="stat-card">
              <h3>Available Courses</h3>
              <p className="stat-number">50+</p>
            </div>
            <div className="stat-card">
              <h3>Active Learners</h3>
              <p className="stat-number">1000+</p>
            </div>
            <div className="stat-card">
              <h3>Success Rate</h3>
              <p className="stat-number">95%</p>
            </div>
          </div>
        </div>

        <div className="section-title">
          <h2>Learning Resources</h2>
          <p>Explore our comprehensive learning tools and resources</p>
        </div>
            
        <div className="cards-container">
          {/* Roadmap Generator Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://upscalegenerator.streamlit.app/')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1492681290082-e932832941e6?ixlib=rb-4.0.3"
                alt="Roadmap Generator"
              />
            </div>
            <div className="card-content">
              <FaRoad className="card-icon" />
              <h3>Roadmap Generator</h3>
              <p>Create your personalized learning path</p>
              <button className="card-button">Generate Roadmap</button>
            </div>
          </div>

          {/* YouTube University Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://universityofyoutube.netlify.app/')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?ixlib=rb-4.0.3"
                alt="YouTube University"
              />
            </div>
            <div className="card-content">
              <FaYoutube className="card-icon" />
              <h3>YouTube University</h3>
              <p>Access curated educational content</p>
              <button className="card-button">Start Learning</button>
            </div>
          </div>

          {/* Quiz Time Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://testerai.streamlit.app/')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1606326608606-aa0b62935f2b?ixlib=rb-4.0.3"
                alt="Quiz Time"
              />
            </div>
            <div className="card-content">
              <FaQuestionCircle className="card-icon" />
              <h3>Quiz Time</h3>
              <p>Test your knowledge and skills</p>
              <button className="card-button">Take Quiz</button>
            </div>
          </div>

          {/* Project Courses Card */}
          <div className="dashboard-card" onClick={() => handleCardClick('https://ashoksuthar14.pythonanywhere.com/employee/dashboard')}>
            <div className="card-image">
              <img 
                src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3"
                alt="Project Courses"
              />
            </div>
            <div className="card-content">
              <FaBook className="card-icon" />
              <h3>Project Courses</h3>
              <p>Hands-on project-based learning</p>
              <button className="card-button">View Courses</button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default EmployeeDashboard; 