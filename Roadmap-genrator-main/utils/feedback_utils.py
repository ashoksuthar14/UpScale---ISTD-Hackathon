# utils/feedback_utils.py
import streamlit as st

def create_feedback_form():
    """Create feedback form elements"""
    feedback = {}
    
    # Ratings
    feedback['relevance_rating'] = st.slider(
        "How relevant was the roadmap to your profile? 🎯",
        1, 5, 3
    )
    
    feedback['clarity_rating'] = st.slider(
        "How clear and easy to follow was the roadmap? 📝",
        1, 5, 3
    )
    
    feedback['actionable_rating'] = st.slider(
        "How actionable were the suggestions? 🎬",
        1, 5, 3
    )
    
    feedback['overall_rating'] = st.slider(
        "Overall rating of the roadmap 🌟",
        1, 5, 3
    )
    
    feedback['feedback_text'] = st.text_area(
        "Any specific feedback or suggestions for improvement? 💭",
        placeholder="What worked well? What could be better?"
    )
    
    return feedback

def enhance_prompt_with_recommendations(base_prompt, recommendations):
    """Enhanced prompt generation based on feedback patterns"""
    if not recommendations:
        return base_prompt
        
    enhanced_prompt = base_prompt + "\n\nBased on analysis of similar successful career roadmaps:"
    
    # Add successful patterns
    if 'successful_patterns' in recommendations:
        patterns = recommendations['successful_patterns']
        
        if patterns.get('skills_focus'):
            enhanced_prompt += f"\n- Focus on these skill areas: {', '.join(patterns['skills_focus'])}"
            
        if patterns.get('timeline_preferences'):
            enhanced_prompt += f"\n- Structure the roadmap with {', '.join(patterns['timeline_preferences'])} goals"
            
        if patterns.get('success_factors'):
            enhanced_prompt += f"\n- Emphasize these success factors: {', '.join(patterns['success_factors'])}"
    
    # Add improvements based on feedback
    if 'improvement_areas' in recommendations:
        improvements = recommendations['improvement_areas']
        enhanced_prompt += "\n\nPlease ensure the roadmap addresses these aspects:"
        
        if improvements.get('clarity', 0) > 50:
            enhanced_prompt += "\n- Provide very clear, step-by-step guidance"
        if improvements.get('specificity', 0) > 50:
            enhanced_prompt += "\n- Include specific, actionable tasks and milestones"
        if improvements.get('timeline', 0) > 50:
            enhanced_prompt += "\n- Clear timeline for each goal and milestone"
        if improvements.get('resources', 0) > 50:
            enhanced_prompt += "\n- Include specific learning resources and materials"
    
    enhanced_prompt += "\n\nEnsure the roadmap is:"
    enhanced_prompt += "\n1. Specific to the user's current role and experience level"
    enhanced_prompt += "\n2. Structured with clear milestones and timelines"
    enhanced_prompt += "\n3. Includes both technical and soft skill development"
    enhanced_prompt += "\n4. Provides actionable next steps and resources"
    
    return enhanced_prompt