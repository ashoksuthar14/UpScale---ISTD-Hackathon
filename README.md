# UpScale-ISTD-Hackathon

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
- **Image**:
  ![Roadmap Generator](path/to/image1.png)
  <img src="img/Roadmap Generator 1" />

#### 2. YouTube University
- **Description**: A distraction-free learning platform that integrates YouTube API to provide courses aligned with the personalized roadmap.
- **Technologies**: YouTube API, React.js.
- **Functionality**:
  - Displays curated courses based on the user’s roadmap.
  - Provides a distraction-free interface to focus on learning.
- **Image**:
  ![YouTube University](path/to/image2.png)

#### 3. Quiz Time
- **Description**: AI-generated quizzes to test knowledge, with adaptive difficulty levels and detailed feedback.
- **Technologies**: LangChain, Gemini API, Streamlit.
- **Functionality**:
  - Generates dynamic quizzes based on the user’s selected courses.
  - Adjusts difficulty based on real-time performance.
  - Awards badges for performance that can be added to profiles.
  - Provides actionable feedback for improvement.
- **Image**:
  ![Quiz Time](path/to/image3.png)

#### 4. Project Course
- **Description**: A feature enabling managers to assign mandatory courses or project-specific training to employees.
- **Technologies**: Flask framework.
- **Functionality**:
  - Managers upload courses such as negotiation, gender sensitization, or project-related technical skills.
  - Employees view and complete assigned courses.
- **Image**:
  ![Project Course](path/to/image4.png)

---

### For Managers:

#### 1. Manager Task Management
- **Description**: A comprehensive AI-powered task management solution.
- **Technologies**: CrewAI, AI Agents, Gemini API, LangChain, Streamlit.
- **Functionality**:
  - One AI agent analyzes project descriptions.
  - Another AI agent breaks projects into tasks.
  - A third agent allocates tasks to employees.
- **Image**:
  ![Manager Task Management](path/to/image5.png)

#### 2. Status Dashboard
- **Description**: A unified dashboard for monitoring employee progress, project statuses, and task completion.
- **Technologies**: Flask framework.
- **Functionality**:
  - Aggregates data from employees, projects, and tasks.
  - Displays real-time progress updates.
  - Allows employees to edit and update progress.
- **Image**:
  ![Status Dashboard](path/to/image6.png)

#### 3. Project Course
- **Description**: Managers assign mandatory and project-specific courses to employees.
- **Functionality**:
  - Similar to the employee-side implementation but with additional managerial controls.
- **Image**:
  ![Project Course (Manager)](path/to/image7.png)

---

### Forum
- **Description**: A community-driven space for employees to ask and answer questions, with features for upvotes and downvotes.
- **Technologies**: Flask framework.
- **Functionality**:
  - Employees post questions.
  - Community members provide answers.
  - Voting system ensures the best answers surface.
- **Image**:
  ![Forum](path/to/image8.png)

---

### AI Coach
- **Description**: An AI chatbot that answers employee questions. If the question is outside its scope, it directs users to the forum.
- **Technologies**: AI model integration.
- **Functionality**:
  - Provides instant answers to queries.
  - Connects users to the forum for unresolved queries.
- **Image**:
  ![AI Coach](path/to/image9.png)

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
5. **Access the Application**:
   Open your browser and navigate to `http://localhost:3000`.

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

