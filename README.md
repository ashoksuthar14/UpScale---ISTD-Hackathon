# UpScale - It's Never Late to Raise the Bar

## Overview

**UpScale** is a cutting-edge project that leverages Artificial Intelligence (AI) to provide personalized learning experiences tailored to workplace environments. It empowers employees to enhance their skills through personalized roadmaps, AI-curated courses, and interactive features. Simultaneously, it equips managers with powerful tools for task management and monitoring. UpScale integrates Machine Learning, Deep Learning, Reinforcement Learning, Generative AI, LangChain, CrewAI, and AI agents to deliver an AI-driven web solution.

---

## Key Features

### For Employees:

#### 1. Roadmap Generator

- **Description**: A tool that creates personalized skill enhancement roadmaps based on the employee’s skills, role, current projects, and career goals.
- **Technologies**: Reinforcement Learning, Gemini API, Streamlit.
- **Functionality**:
  - Utilizes Reinforcement Learning to adaptively refine roadmaps based on user feedback and learning progress.
  - Collects input data from users (skills, role, goals, feedback).
  - Generates a tailored roadmap optimized for achieving career milestones.
  - Updates the roadmap based on feedback for continuous improvement.
- **Images**:
  <div style="display: flex;">
    <img src="img/Roadmap Generator 0.png" alt="Roadmap Generator 0" width="200" />
    <img src="img/Roadmap Generator 1.png" alt="Roadmap Generator 1" width="200" />
    <img src="img/Roadmap Generator 2.png" alt="Roadmap Generator 2" width="200" />
    <img src="img/Roadmap Generator 3.png" alt="Roadmap Generator 3" width="200" />
  </div>

#### 2. YouTube University

- **Description**: A distraction-free learning platform that integrates YouTube API to provide courses aligned with the personalized roadmap.
- **Technologies**: YouTube API, React.js.
- **Functionality**:
  - Displays curated courses based on the user’s roadmap.
  - Provides a distraction-free interface to focus on learning.
- **Images**:
  <div style="display: flex;">
    <img src="img/Youtube `1.png" alt="Youtube 1" width="200" />
    <img src="img/youtube 2.png" alt="Youtube 2" width="200" />
  </div>

#### 3. Quiz Time

- **Description**: AI-generated quizzes to test knowledge, with adaptive difficulty levels and detailed feedback.
- **Technologies**: LangChain, Gemini API, Streamlit.
- **Functionality**:
  - Generates dynamic quizzes based on the user’s selected courses.
  - Adjusts difficulty based on real-time performance.
  - Awards badges for performance that can be added to profiles.
  - Provides actionable feedback for improvement.
- **Images**:
  <div style="display: flex;">
    <img src="img/test1.png" alt="Test 1" width="200" />
    <img src="img/test2.png" alt="Test 2" width="200" />
    <img src="img/test3.png" alt="Test 3" width="200" />
  </div>

#### 4. Project Course

- **Description**: A feature enabling managers to assign mandatory courses or project-specific training to employees.
- **Technologies**: Flask framework.
- **Functionality**:
  - Managers upload courses such as negotiation, gender sensitization, or project-related technical skills.
  - Employees view and complete assigned courses.
  - **Test Credentials for Employees**:
    - Email: [bob@example.com](mailto:bob@example.com)
    - Password: password124
- **Images**:
  <div style="display: flex;">
    <img src="img/project course 1.png" alt="Project Course 1" width="200" />
    <img src="img/project course 2.png" alt="Project Course 2" width="200" />
  </div>

---

### For Managers:

#### 1. Manager Task Management

- **Description**: A comprehensive AI-powered task management solution.
- **Technologies**: CrewAI, AI Agents, Gemini API, LangChain, Streamlit.
- **Functionality**:
  - One AI agent analyzes project descriptions.
  - Another AI agent breaks projects into tasks.
  - A third agent allocates tasks to employees.
- **Images**:
  <div style="display: flex;">
    <img src="img/manager1.png" alt="Manager 1" width="200" />
    <img src="img/manager2.png" alt="Manager 2" width="200" />
    <img src="img/manager3.png" alt="Manager 3" width="200" />
    <img src="img/manager4.png" alt="Manager 4" width="200" />
  </div>

#### 2. Status Dashboard

- **Description**: A unified dashboard for monitoring employee progress, project statuses, and task completion.
- **Technologies**: Flask framework.
- **Functionality**:
  - Aggregates data from employees, projects, and tasks.
  - Displays real-time progress updates.
  - Allows employees to edit and update progress.
- **Images**:
  <div style="display: flex;">
    <img src="img/status 1.png" alt="Status 1" width="200" />
    <img src="img/status 2.png" alt="Status 2" width="200" />
  </div>

#### 3. Project Course

- **Description**: Managers assign mandatory and project-specific courses to employees.
- **Functionality**:
  - Similar to the employee-side implementation but with additional managerial controls.
  - **Test Credentials for Managers**:
    - Email: [manager@example.com](mailto:manager@example.com)
    - Password: password123
- **Images**:
  <div style="display: flex;">
    <img src="img/manager project course 1.png" alt="Manager Project Course 1" width="200" />
  </div>

---

### Forum

- **Description**: A community-driven space for employees to ask and answer questions, with features for upvotes and downvotes.
- **Technologies**: Flask framework.
- **Functionality**:
  - Employees post questions.
  - Community members provide answers.
  - Voting system ensures the best answers surface.
- **Images**:
  <div style="display: flex;">
    <img src="img/Forum 2.png" alt="Forum 2" width="200" />
  </div>

---

### AI Coach

- **Description**: An AI chatbot that answers employee questions. If the question is outside its scope, it directs users to the forum.
- **Technologies**: AI model integration.
- **Functionality**:
  - Provides instant answers to queries.
  - Connects users to the forum for unresolved queries.
- **Images**:
  <div style="display: flex;">
    <img src="img/Forum 2.png" alt="AI Coach Forum 2" width="200" />
  </div>

---

## Tech Stack

- **Frontend**: React.js, Tailwind CSS.
- **Backend**: Flask.
- **Database**: PostgreSQL, SQLite, SQLAlchemy.
- **AI Tools**: LangChain, CrewAI, Gemini API, Reinforcement Learning.
- **Learning API**: YouTube API.
- **Frameworks**: Streamlit.

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/upscale.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   npm install
   ```
3. **Start Backend Server**:
   ```bash
   flask run
   ```
4. **Start Frontend Server**:
   ```bash
   npm start
   ```
5. **Access the Application**: Open your browser and navigate to `http://localhost:3000`.

---

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes and submit a pull request.
4. Ensure your code follows the existing coding standards.

---

## Future Enhancements

- Integration with third-party LMS platforms.
- Advanced analytics for managers.
- Gamification elements for employee engagement.
- Multi-language support.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**UpScale** is your one-stop solution to elevate workplace learning and management using the power of AI. Raise the bar today!

