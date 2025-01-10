# models/reinforcement_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import os

class RoadmapReinforcementModel:
    def __init__(self, feedback_path='data/feedback_data.csv'):
        self.feedback_path = feedback_path
        self.label_encoders = {}
        self.model = RandomForestClassifier()
        
        # Initialize columns for feedback data
        self.columns = [
            'role', 'company_type', 'experience_level', 'skills_count',
            'goals_type', 'relevance_rating', 'clarity_rating',
            'actionable_rating', 'overall_rating', 'feedback_text'
        ]
        
        self.load_feedback_data()
    
    def load_feedback_data(self):
        """Load or create feedback dataset"""
        try:
            # Create data directory if it doesn't exist
            os.makedirs(os.path.dirname(self.feedback_path), exist_ok=True)
            
            # Try to load existing data
            if os.path.exists(self.feedback_path) and os.path.getsize(self.feedback_path) > 0:
                self.feedback_data = pd.read_csv(self.feedback_path)
            else:
                # Create new empty DataFrame with defined columns
                self.feedback_data = pd.DataFrame(columns=self.columns)
                # Save empty DataFrame to create the file
                self.feedback_data.to_csv(self.feedback_path, index=False)
                
        except Exception as e:
            print(f"Error loading feedback data: {str(e)}")
            # Create new empty DataFrame if there's any error
            self.feedback_data = pd.DataFrame(columns=self.columns)
    
    def preprocess_input(self, data):
        """Preprocess input data for model"""
        features = {
            'role': data['role'].lower(),
            'company_type': self._categorize_company(data['company']),
            'experience_level': self._extract_experience_level(data['role']),
            'goals_type': self._categorize_goals(data['goals']),
            'skills_count': len(data['skills'].split(','))
        }
        return features
    
    def _categorize_company(self, company):
        """Categorize company type"""
        company = company.lower()
        if any(term in company for term in ['google', 'amazon', 'microsoft', 'apple', 'meta']):
            return 'tech_giant'
        elif any(term in company for term in ['startup', 'technologies', 'tech']):
            return 'tech_startup'
        else:
            return 'other'
    
    def _extract_experience_level(self, role):
        """Extract experience level from role"""
        role = role.lower()
        if any(level in role for level in ['senior', 'lead', 'principal']):
            return 'senior'
        elif any(level in role for level in ['junior', 'associate']):
            return 'junior'
        else:
            return 'mid'
    
    def _categorize_goals(self, goals):
        """Categorize career goals"""
        goals = goals.lower()
        if any(term in goals for term in ['manage', 'lead', 'leadership']):
            return 'leadership'
        elif any(term in goals for term in ['technical', 'expert', 'specialist']):
            return 'technical_expert'
        else:
            return 'growth'
            
    def get_recommendations(self, user_data):
        """Get recommendations based on historical feedback with fuzzy matching"""
        if len(self.feedback_data) < 2:  # Reduced minimum feedback requirement
            return None
            
        features = self.preprocess_input(user_data)
        
        # Calculate similarity scores for all feedback entries
        similar_profiles = []
        for _, feedback in self.feedback_data.iterrows():
            similarity_score = self._calculate_similarity(features, feedback)
            if similarity_score > 0.5:  # Similarity threshold
                similar_profiles.append({
                    'feedback': feedback,
                    'similarity': similarity_score
                })
        
        # Sort by similarity and get top matches
        similar_profiles.sort(key=lambda x: x['similarity'], reverse=True)
        top_profiles = similar_profiles[:5]  # Get top 5 similar profiles
        
        if not top_profiles:
            return None
            
        # Extract patterns from successful similar roadmaps
        successful_patterns = self._analyze_successful_patterns(top_profiles)
        
        # Extract improvement areas from negative feedback
        improvement_areas = self._analyze_improvement_areas(top_profiles)
        
        return {
            'successful_patterns': successful_patterns,
            'improvement_areas': improvement_areas,
            'sample_size': len(top_profiles)
        }
    
    def _calculate_similarity(self, features, feedback):
        """Calculate similarity score between current user and feedback entry"""
        score = 0.0
        
        # Role similarity (partial matching)
        if features['role'].lower() in feedback['role'].lower() or \
           feedback['role'].lower() in features['role'].lower():
            score += 0.3
        
        # Experience level match
        if features['experience_level'] == feedback['experience_level']:
            score += 0.2
            
        # Company type match
        if features['company_type'] == feedback['company_type']:
            score += 0.2
            
        # Goals type match
        if features['goals_type'] == feedback['goals_type']:
            score += 0.3
            
        return score
    
    def _analyze_successful_patterns(self, similar_profiles):
        """Analyze patterns from highly-rated similar roadmaps"""
        patterns = {
            'skills_focus': [],
            'timeline_preferences': [],
            'learning_resources': [],
            'success_factors': []
        }
        
        for profile in similar_profiles:
            feedback = profile['feedback']
            if feedback['overall_rating'] >= 4:
                # Extract insights from feedback text
                feedback_text = feedback['feedback_text'].lower()
                
                # Analyze skills focus
                if 'technical' in feedback_text:
                    patterns['skills_focus'].append('technical_depth')
                if 'soft skills' in feedback_text:
                    patterns['skills_focus'].append('soft_skills')
                    
                # Analyze timeline preferences
                if 'long term' in feedback_text:
                    patterns['timeline_preferences'].append('long_term')
                if 'short term' in feedback_text:
                    patterns['timeline_preferences'].append('short_term')
                    
                # Add other pattern analysis as needed
        
        # Count and sort patterns by frequency
        for category in patterns:
            patterns[category] = self._get_top_patterns(patterns[category])
            
        return patterns
    
    def _analyze_improvement_areas(self, similar_profiles):
        """Analyze common improvement areas from lower-rated roadmaps"""
        improvements = {
            'clarity': 0,
            'specificity': 0,
            'timeline': 0,
            'resources': 0
        }
        
        for profile in similar_profiles:
            feedback = profile['feedback']
            if feedback['overall_rating'] < 4:
                feedback_text = feedback['feedback_text'].lower()
                
                if 'clear' in feedback_text or 'clarity' in feedback_text:
                    improvements['clarity'] += 1
                if 'specific' in feedback_text or 'concrete' in feedback_text:
                    improvements['specificity'] += 1
                if 'timeline' in feedback_text or 'time' in feedback_text:
                    improvements['timeline'] += 1
                if 'resource' in feedback_text or 'material' in feedback_text:
                    improvements['resources'] += 1
        
        # Convert to percentage-based recommendations
        total_low_ratings = sum(1 for p in similar_profiles if p['feedback']['overall_rating'] < 4)
        if total_low_ratings > 0:
            for key in improvements:
                improvements[key] = (improvements[key] / total_low_ratings) * 100
                
        return improvements
    
    def _get_top_patterns(self, pattern_list, top_n=3):
        """Get top N most frequent patterns"""
        if not pattern_list:
            return []
        return [item for item, count in Counter(pattern_list).most_common(top_n)]
    
    def save_feedback(self, user_data, feedback_data):
        """Save user feedback"""
        try:
            # Preprocess user data
            features = self.preprocess_input(user_data)
            
            # Combine features with feedback
            feedback_entry = {
                **features,
                'relevance_rating': feedback_data['relevance_rating'],
                'clarity_rating': feedback_data['clarity_rating'],
                'actionable_rating': feedback_data['actionable_rating'],
                'overall_rating': feedback_data['overall_rating'],
                'feedback_text': feedback_data['feedback_text']
            }
            
            # Create DataFrame with single feedback entry
            new_feedback = pd.DataFrame([feedback_entry])
            
            # Concatenate with existing feedback data
            self.feedback_data = pd.concat([self.feedback_data, new_feedback], ignore_index=True)
            
            # Save updated feedback data
            self.feedback_data.to_csv(self.feedback_path, index=False)
            
            return True
            
        except Exception as e:
            print(f"Error saving feedback: {str(e)}")
            return False