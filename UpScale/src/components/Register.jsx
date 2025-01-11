/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Auth.css';

const Register = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    role: ''
  });
  const [showPopup, setShowPopup] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    setShowPopup(true);
    
    // Navigate after 2 seconds
    setTimeout(() => {
      if (formData.role === 'manager') {
        navigate('/manager');
      } else if (formData.role === 'employee') {
        navigate('/employee');
      }
    }, 2000);
  };

  return (
    <div className="auth-page">
      {showPopup && (
        <div className="popup-overlay">
          <div className="popup">
            <h3>Success!</h3>
            <p>Your account has been created successfully.</p>
            <div className="loading-dots">
              <span>.</span><span>.</span><span>.</span>
            </div>
          </div>
        </div>
      )}
      
      <div className="auth-container">
        <form onSubmit={handleSubmit} className="auth-form">
          <h2>Create Account</h2>
          <p className="subtitle">Join AI Learning Platform</p>
          
          <div className="form-group">
            <label>Full Name</label>
            <input
              type="text"
              name="name"
              placeholder="Enter your full name"
              value={formData.name}
              onChange={(e) => setFormData({...formData, name: e.target.value})}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              name="email"
              placeholder="Enter your email"
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              name="password"
              placeholder="Create a password"
              value={formData.password}
              onChange={(e) => setFormData({...formData, password: e.target.value})}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Confirm Password</label>
            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm your password"
              value={formData.confirmPassword}
              onChange={(e) => setFormData({...formData, confirmPassword: e.target.value})}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Select Role</label>
            <div className="role-group">
              <label className="role-option">
                <input
                  type="radio"
                  name="role"
                  value="employee"
                  checked={formData.role === 'employee'}
                  onChange={(e) => setFormData({...formData, role: e.target.value})}
                  required
                />
                <span>Employee</span>
              </label>
              <label className="role-option">
                <input
                  type="radio"
                  name="role"
                  value="manager"
                  checked={formData.role === 'manager'}
                  onChange={(e) => setFormData({...formData, role: e.target.value})}
                />
                <span>Manager</span>
              </label>
            </div>
          </div>
          
          <button type="submit" className="submit-btn">Create Account</button>
          
          <p className="auth-link">
            Already have an account? <Link to="/login">Sign In</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Register; 