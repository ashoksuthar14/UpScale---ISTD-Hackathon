from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Use SQLite for development, MySQL/PostgreSQL for production
if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    # PythonAnywhere MySQL configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Ashoksuthar:<your-mysql-password>@Ashoksuthar.mysql.pythonanywhere-services.com/Ashoksuthar$forum'
else:
    # Local SQLite configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'forum.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Question(db.Model):
    __tablename__ = 'questions'  # Explicitly set table name
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    votes = db.Column(db.Integer, default=0)
    answers = db.relationship('Answer', backref='question', lazy=True, cascade='all, delete-orphan')

class Answer(db.Model):
    __tablename__ = 'answers'  # Explicitly set table name
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    votes = db.Column(db.Integer, default=0)

def init_db():
    # Delete the database file if it exists
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'forum.db')
    if os.path.exists(db_file):
        os.remove(db_file)
    
    # Create all tables
    db.create_all()
    
    # Add some sample data
    sample_question = Question(
        title="Welcome to UpScale Forum",
        content="This is a sample question to get started.",
        author_name="Admin"
    )
    db.session.add(sample_question)
    db.session.commit()

@app.route('/')
def home():
    questions = Question.query.order_by(Question.created_at.desc()).all()
    return render_template('home.html', questions=questions)

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author_name = request.form.get('author_name')
        question = Question(title=title, content=content, author_name=author_name)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('ask.html')

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method == 'POST':
        content = request.form.get('content')
        author_name = request.form.get('author_name')
        answer = Answer(content=content, author_name=author_name, question=question)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question', question_id=question_id))
    return render_template('question.html', question=question)

@app.route('/vote/<string:type>/<int:id>/<int:value>')
def vote(type, id, value):
    if type == 'question':
        item = Question.query.get_or_404(id)
    else:
        item = Answer.query.get_or_404(id)
    
    item.votes += value
    db.session.commit()
    return jsonify({'votes': item.votes})

# Only run init_db() in development
if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True) 