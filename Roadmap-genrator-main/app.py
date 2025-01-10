# app.py
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from models.reinforcement_model import RoadmapReinforcementModel
from utils.feedback_utils import create_feedback_form, enhance_prompt_with_recommendations

# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Career Roadmap Generator",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state variables
if 'roadmap' not in st.session_state:
    st.session_state.roadmap = None
if 'user_info' not in st.session_state:
    st.session_state.user_info = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'feedback_submitted' not in st.session_state:
    st.session_state.feedback_submitted = False

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize reinforcement model
@st.cache_resource
def get_reinforcement_model():
    return RoadmapReinforcementModel()

def generate_roadmap(user_info, reinforcement_model):
    """Generate roadmap using Gemini API with reinforcement learning"""
    try:
        recommendations = reinforcement_model.get_recommendations(user_info)
        
        base_prompt = f"""
        Create a detailed career roadmap for a professional with the following profile:
        
        Current Role: {user_info['role']}
        Company: {user_info['company']}
        Current Skills: {user_info['skills']}
        Recent Projects: {user_info['projects']}
        Career Goals: {user_info['goals']}
        
        Please provide:
        1. A 6-month action plan
        2. Key skills to develop
        3. Recommended learning resources
        4. Career milestones to aim for
        5. Potential challenges and how to overcome them
        
        Format the response with clear headings and bullet points.
        """
        
        final_prompt = enhance_prompt_with_recommendations(base_prompt, recommendations)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(final_prompt)
        
        return response.text, recommendations
    
    except Exception as e:
        st.error(f"Error generating roadmap: {str(e)}")
        return None, None

def handle_feedback_submission(feedback, user_info, reinforcement_model):
    if feedback['feedback_text']:
        reinforcement_model.save_feedback(user_info, feedback)
        st.session_state.feedback_submitted = True
        st.success("Thank you for your feedback! It will help improve future roadmaps.")
    else:
        st.warning("Please provide some text feedback before submitting.")

def main():
    reinforcement_model = get_reinforcement_model()
    
    st.markdown("""
        <h1 style='text-align: center;'>AI-Powered Career Roadmap Generator 🎯</h1>
        """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.title("About")
        st.info(
            "This tool uses Google's Gemini AI and reinforcement learning to create "
            "personalized career roadmaps based on your profile and community feedback."
        )
        
        if os.path.exists('data/feedback_data.csv'):
            st.success(f"Learning from {len(reinforcement_model.feedback_data)} previous roadmaps")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Your Professional Profile")
        with st.form("user_input_form"):
            role = st.text_input(
                "Current Role",
                placeholder="e.g., Senior Software Engineer"
            )
            
            company = st.text_input(
                "Company",
                placeholder="e.g., Tech Corp Inc."
            )
            
            skills = st.text_area(
                "Current Skills",
                placeholder="e.g., Python, React, AWS, Project Management"
            )
            
            projects = st.text_area(
                "Recent Projects",
                placeholder="Describe 2-3 key projects you've worked on"
            )
            
            goals = st.text_area(
                "Career Goals",
                placeholder="What do you want to achieve in your career?"
            )
            
            submit_button = st.form_submit_button("Generate Roadmap")
    
    with col2:
        st.subheader("Tips for Better Results")
        st.markdown("""
        - Be specific about your current role
        - List skills in order of expertise
        - Include both technical and soft skills
        - Be clear about your career goals
        - Mention timeframes if applicable
        """)
    
    # Handle form submission for roadmap generation
    if submit_button:
        if not all([role, company, skills, projects, goals]):
            st.error("Please fill in all fields to generate your roadmap.")
        else:
            user_info = {
                "role": role,
                "company": company,
                "skills": skills,
                "projects": projects,
                "goals": goals
            }
            
            with st.spinner("Generating your personalized career roadmap..."):
                roadmap, recommendations = generate_roadmap(user_info, reinforcement_model)
                
                if roadmap:
                    # Store in session state
                    st.session_state.roadmap = roadmap
                    st.session_state.user_info = user_info
                    st.session_state.recommendations = recommendations
                    st.session_state.feedback_submitted = False
    
    # Display roadmap and feedback form if available
    if st.session_state.roadmap:
        st.success("Your career roadmap has been generated!")
        
        if st.session_state.recommendations:
            st.info(
                f"This roadmap was enhanced based on feedback from "
                f"{st.session_state.recommendations.get('sample_size', 0)} similar profiles!"
            )
        
        st.markdown("---")
        st.markdown("### Your Personalized Career Roadmap")
        st.markdown(st.session_state.roadmap)
        
        st.download_button(
            label="Download Roadmap",
            data=st.session_state.roadmap,
            file_name="career_roadmap.txt",
            mime="text/plain"
        )
        
        # Only show feedback form if feedback hasn't been submitted
        if not st.session_state.feedback_submitted:
            st.markdown("---")
            st.markdown("### Help Us Improve! 📝")
            st.write(
                "Your feedback helps us generate better roadmaps for the community."
            )
            
            feedback = create_feedback_form()
            
            if st.button("Submit Feedback"):
                handle_feedback_submission(
                    feedback,
                    st.session_state.user_info,
                    reinforcement_model
                )

if __name__ == "__main__":
    main()