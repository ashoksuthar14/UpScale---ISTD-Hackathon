from app.routes import employee
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import ProjectAssignment, CourseProgress, Project, Course
from app import db

@employee.route('/dashboard')
@login_required
def dashboard():
    assignments = ProjectAssignment.query.filter_by(employee_id=current_user.id).all()
    course_progress = CourseProgress.query.filter_by(user_id=current_user.id).all()
    return render_template('employee/dashboard.html', 
                         assignments=assignments,
                         course_progress=course_progress)

@employee.route('/courses')
@login_required
def courses():
    course_progress = CourseProgress.query.filter_by(user_id=current_user.id).all()
    return render_template('employee/courses.html', course_progress=course_progress)

@employee.route('/update_course_status/<int:progress_id>/<string:status>')
@login_required
def update_course_status(progress_id, status):
    progress = CourseProgress.query.get_or_404(progress_id)
    if progress.user_id != current_user.id:
        flash('You do not have permission to update this course.')
        return redirect(url_for('employee.courses'))
    
    progress.status = status
    db.session.commit()
    flash('Course status updated successfully!')
    return redirect(url_for('employee.courses')) 