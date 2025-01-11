/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Auth.css';

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    role: ''
  });
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Direct navigation based on role
    if (formData.role === 'manager') {
      navigate('/manager');
    } else if (formData.role === 'employee') {
      navigate('/employee');
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-container">
        <form onSubmit={handleSubmit} className="auth-form">
          <h2>Sign In</h2>
          <p className="subtitle">Welcome back to AI Learning Platform</p>
          
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
              placeholder="Enter your password"
              value={formData.password}
              onChange={(e) => setFormData({...formData, password: e.target.value})}
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
          
          <button type="submit" className="submit-btn">Sign In</button>
          
          <p className="auth-link">
            Don't have an account? <Link to="/register">Register</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login; 