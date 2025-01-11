/* eslint-disable no-unused-vars */
import React from 'react';
import { FaUser, FaUsers, FaProjectDiagram, FaEnvelope, FaBriefcase } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import './ManagerProfile.css';

const ManagerProfile = () => {
  const managerData = {
    name: "Jane Doe",
    role: "Senior Project Manager",
    photo: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3",
    teams: {
      development: [
        { name: "John Smith", role: "Frontend Developer", photo: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3" },
        { name: "Emily Brown", role: "Backend Developer", photo: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3" },
        { name: "Michael Lee", role: "UI/UX Designer", photo: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3" }
      ],
      marketing: [
        { name: "Sarah Johnson", role: "Marketing Specialist", photo: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3" },
        { name: "David Wilson", role: "Content Creator", photo: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3" }
      ]
    },
    projects: [
      {
        name: "E-commerce Platform",
        category: "Web Development",
        status: "In Progress"
      },
      {
        name: "Mobile App Redesign",
        category: "UI/UX Design",
        status: "Planning"
      },
      {
        name: "Data Analytics Dashboard",
        category: "Data Visualization",
        status: "Testing"
      }
    ]
  };

  return (
    <div className="profile-page">
      <nav className="profile-nav">
        <div className="nav-content">
          <div className="logo">Manager Profile</div>
          <Link to="/manager" className="back-link">Back to Dashboard</Link>
        </div>
      </nav>

      <h1 className="page-title">Manager Profile</h1>

      <div className="profile-content">
        {/* Profile Section */}
        <div className="profile-section">
          <div className="profile-photo">
            <img src={managerData.photo} alt={managerData.name} />
          </div>
          <div className="profile-info">
            <h2>{managerData.name}</h2>
            <p className="role">{managerData.role}</p>
          </div>
        </div>

        {/* Teams Section */}
        <div className="teams-section">
          <h2>Teams</h2>
          
          {/* Development Team */}
          <div className="team-group">
            <h3>Development Team</h3>
            <div className="team-members">
              {managerData.teams.development.map((member, index) => (
                <div key={index} className="member-item">
                  <div className="member-photo">
                    <img src={member.photo} alt={member.name} />
                  </div>
                  <div className="member-details">
                    <h4>{member.name}</h4>
                    <p>{member.role}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Marketing Team */}
          <div className="team-group">
            <h3>Marketing Team</h3>
            <div className="team-members">
              {managerData.teams.marketing.map((member, index) => (
                <div key={index} className="member-item">
                  <div className="member-photo">
                    <img src={member.photo} alt={member.name} />
                  </div>
                  <div className="member-details">
                    <h4>{member.name}</h4>
                    <p>{member.role}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Projects Section */}
        <div className="projects-section">
          <h2>Projects</h2>
          <div className="projects-grid">
            {managerData.projects.map((project, index) => (
              <div key={index} className="project-card">
                <h3>{project.name}</h3>
                <span className="project-category">{project.category}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ManagerProfile; 