/* eslint-disable no-unused-vars */
import React from 'react';
import { FaAward, FaCode, FaBrain, FaBullseye, FaBolt, FaUsers, FaRocket, FaStar } from 'react-icons/fa';
import './EmployeeProfile.css';

const EmployeeProfile = () => {
  const employeeData = {
    name: "John Doe",
    email: "john.doe@example.com",
    photo: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3",
    role: "Senior Software Developer",
    companyName: "Tech Innovations Inc.",
    skills: [
      { name: "JavaScript", level: 90 },
      { name: "React", level: 85 },
      { name: "Node.js", level: 80 },
      { name: "TypeScript", level: 75 },
    ],
    projects: [
      { name: "E-commerce Platform", role: "Frontend Developer" },
      { name: "CRM System", role: "Full Stack Developer" },
      { name: "Mobile App", role: "React Native Developer" },
    ],
    badges: [
      { type: 'achievement', name: 'Top Performer', icon: <FaAward />, color: 'yellow' },
      { type: 'skill', name: 'Coding Expert', icon: <FaCode />, color: 'blue' },
      { type: 'learning', name: 'Quick Learner', icon: <FaBrain />, color: 'green' },
      { type: 'goal', name: 'Goal Crusher', icon: <FaBullseye />, color: 'red' },
      { type: 'innovation', name: 'Innovator', icon: <FaBolt />, color: 'purple' },
      { type: 'teamwork', name: 'Team Player', icon: <FaUsers />, color: 'indigo' },
      { type: 'project', name: 'Project Master', icon: <FaRocket />, color: 'orange' },
      { type: 'excellence', name: 'Excellence', icon: <FaStar />, color: 'pink' },
    ],
  };

  return (
    <div className="profile-container">
      <h1 className="profile-title">Employee Profile</h1>
      <div className="profile-grid">
        {/* Left Column - Photo and Basic Info */}
        <div className="profile-info-card">
          <div className="profile-photo">
            <img src={employeeData.photo} alt={employeeData.name} />
          </div>
          <h2 className="profile-name">{employeeData.name}</h2>
          <p className="profile-email">{employeeData.email}</p>
          <p className="profile-role">{employeeData.role}</p>
          <p className="profile-company">{employeeData.companyName}</p>
        </div>

        {/* Right Column - Badges, Skills, Projects */}
        <div className="profile-details">
          {/* Badges Section */}
          <div className="profile-card">
            <h3 className="card-title">Employee Badges</h3>
            <div className="badges-grid">
              {employeeData.badges.map((badge, index) => (
                <div key={index} className={`badge-item badge-${badge.color}`}>
                  <div className="badge-icon">{badge.icon}</div>
                  <span className="badge-type">{badge.type}</span>
                  <div className="badge-tooltip">{badge.name}</div>
                </div>
              ))}
            </div>
          </div>

          {/* Skills Section */}
          <div className="profile-card">
            <h3 className="card-title">Skills</h3>
            <div className="skills-list">
              {employeeData.skills.map((skill, index) => (
                <div key={index} className="skill-item">
                  <div className="skill-header">
                    <span className="skill-name">{skill.name}</span>
                    <span className="skill-level">{skill.level}%</span>
                  </div>
                  <div className="skill-bar">
                    <div 
                      className="skill-progress" 
                      style={{ width: `${skill.level}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Projects Section */}
          <div className="profile-card">
            <h3 className="card-title">Projects</h3>
            <div className="projects-list">
              {employeeData.projects.map((project, index) => (
                <div key={index} className="project-item">
                  <span className="project-name">{project.name}</span>
                  <span className="project-role">{project.role}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EmployeeProfile; 