from app.routes import manager
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired
from app.models import Project, User, ProjectAssignment, Course, CourseProgress
from app import db

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create Project')

class AssignEmployeeForm(FlaskForm):
    employees = SelectMultipleField('Select Employees', coerce=int)
    submit = SubmitField('Assign Employees')

class CourseAssignmentForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('technical', 'Technical'),
        ('soft_skills', 'Soft Skills')
    ])
    platform = SelectField('Platform', choices=[
        ('google', 'Google Skill Boost'),
        ('aws', 'AWS'),
        ('microsoft', 'Microsoft'),
        ('other', 'Other')
    ])
    is_mandatory = SelectField('Is Mandatory', choices=[
        ('yes', 'Yes'),
        ('no', 'No')
    ])
    employees = SelectMultipleField('Assign to Employees', coerce=int)
    submit = SubmitField('Assign Course')

@manager.route('/dashboard')
@login_required
def dashboard():
    projects = Project.query.filter_by(manager_id=current_user.id).all()
    return render_template('manager/dashboard.html', projects=projects)

@manager.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            manager_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!')
        return redirect(url_for('manager.dashboard'))
    return render_template('manager/create_project.html', form=form)

@manager.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    return render_template('manager/edit_project.html')

@manager.route('/assign_courses/<int:project_id>', methods=['GET', 'POST'])
@login_required
def assign_courses(project_id):
    project = Project.query.get_or_404(project_id)
    if project.manager_id != current_user.id:
        flash('You do not have permission to modify this project.')
        return redirect(url_for('manager.dashboard'))
    
    form = CourseAssignmentForm()
    
    # Get all employees assigned to this project
    project_employee_ids = [a.employee_id for a in project.assignments]
    employees = User.query.filter(User.id.in_(project_employee_ids)).all()
    form.employees.choices = [(e.id, e.username) for e in employees]
    
    if form.validate_on_submit():
        print(f"\nCreating new course for project {project.name} (ID: {project.id})")
        # Create new course
        course = Course(
            name=form.course_name.data,
            description=form.description.data,
            category=form.category.data,
            platform=form.platform.data,
            is_mandatory=(form.is_mandatory.data == 'yes')
        )
        db.session.add(course)
        db.session.flush()  # Get the course ID
        print(f"Created course: {course.name} (ID: {course.id})")
        
        # Assign course to selected employees
        print(f"Selected employee IDs: {form.employees.data}")
        for employee_id in form.employees.data:
            progress = CourseProgress(
                user_id=employee_id,
                course_id=course.id,
                status='Not Started'
            )
            db.session.add(progress)
            print(f"Added course progress for employee ID: {employee_id}")
        
        db.session.commit()
        flash('Course assigned successfully!')
        return redirect(url_for('manager.dashboard'))
    
    # Get existing courses for this project's employees
    existing_courses = Course.query.join(CourseProgress)\
        .filter(CourseProgress.user_id.in_(project_employee_ids))\
        .distinct().all()
    
    return render_template('manager/assign_courses.html', 
                         form=form, 
                         project=project, 
                         existing_courses=existing_courses,
                         employees=employees)

@manager.route('/assign_employee/<int:project_id>', methods=['GET', 'POST'])
@login_required
def assign_employee(project_id):
    project = Project.query.get_or_404(project_id)
    if project.manager_id != current_user.id:
        flash('You do not have permission to modify this project.')
        return redirect(url_for('manager.dashboard'))
    
    form = AssignEmployeeForm()
    
    # Get all employees (non-manager users)
    employees = User.query.filter_by(is_manager=False).all()
    form.employees.choices = [(e.id, e.username) for e in employees]
    
    if form.validate_on_submit():
        print(f"\nAssigning employees to project {project.name} (ID: {project.id})")
        print(f"Selected employee IDs: {form.employees.data}")
        
        # Remove unselected employees
        ProjectAssignment.query.filter_by(project_id=project.id).delete()
        
        # Add selected employees
        for employee_id in form.employees.data:
            assignment = ProjectAssignment(project_id=project.id, employee_id=employee_id)
            db.session.add(assignment)
            print(f"Added assignment for employee ID: {employee_id}")
        
        db.session.commit()
        flash('Team members updated successfully!')
        return redirect(url_for('manager.dashboard'))
    
    # Pre-select currently assigned employees
    assigned_ids = [a.employee_id for a in project.assignments]
    form.employees.data = assigned_ids
    
    return render_template('manager/assign_employee.html', form=form, project=project) 