from app import create_app, db
from app.models import User, Project, Course, ProjectAssignment, CourseProgress

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User,
        'Project': Project,
        'Course': Course,
        'ProjectAssignment': ProjectAssignment,
        'CourseProgress': CourseProgress
    }

if __name__ == '__main__':
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        # Create a test manager if none exists
        if not User.query.filter_by(email='manager@example.com').first():
            manager = User(
                username='manager',
                email='manager@example.com',
                is_manager=True
            )
            manager.set_password('password123')
            db.session.add(manager)
            db.session.flush()  # Get the manager ID
            
            # Create a test project for the manager
            project = Project(
                name='Test Project',
                description='This is a test project',
                manager_id=manager.id
            )
            db.session.add(project)
            db.session.flush()  # Get the project ID
            print(f"Created project with ID: {project.id}")
            
            # Create test employees
            test_employees = [
                {
                    'username': 'john_doe',
                    'email': 'john@example.com',
                    'password': 'password123'
                },
                {
                    'username': 'jane_smith',
                    'email': 'jane@example.com',
                    'password': 'password123'
                },
                {
                    'username': 'bob_wilson',
                    'email': 'bob@example.com',
                    'password': 'password123'
                }
            ]
            
            for emp_data in test_employees:
                employee = User(
                    username=emp_data['username'],
                    email=emp_data['email'],
                    is_manager=False
                )
                employee.set_password(emp_data['password'])
                db.session.add(employee)
                db.session.flush()  # Get the employee ID
                print(f"Created employee {employee.username} with ID: {employee.id}")
                
                # Assign employee to the test project
                assignment = ProjectAssignment(
                    project_id=project.id,
                    employee_id=employee.id
                )
                db.session.add(assignment)
                print(f"Assigned employee {employee.username} to project {project.name}")
                
                # Create a test course and assign it to the employee
                course = Course(
                    name=f'Test Course for {employee.username}',
                    description='This is a test course',
                    category='technical',
                    platform='google',
                    is_mandatory=True
                )
                db.session.add(course)
                db.session.flush()  # Get the course ID
                print(f"Created course with ID: {course.id}")
                
                # Create course progress
                progress = CourseProgress(
                    user_id=employee.id,
                    course_id=course.id,
                    status='Not Started'
                )
                db.session.add(progress)
                print(f"Created course progress for {employee.username}")
            
            try:
                db.session.commit()
                print("\nAll test data created successfully!")
                print("\nManager account:")
                print("Email: manager@example.com")
                print("Password: password123")
                print("\nEmployee accounts:")
                for emp in test_employees:
                    print(f"Email: {emp['email']}")
                    print(f"Password: {emp['password']}")
                    print("---")
                
                # Verify data
                print("\nVerifying data:")
                for emp in User.query.filter_by(is_manager=False).all():
                    print(f"\nEmployee: {emp.username}")
                    assignments = ProjectAssignment.query.filter_by(employee_id=emp.id).all()
                    print(f"Project assignments: {len(assignments)}")
                    for a in assignments:
                        print(f"- Project: {a.project.name}")
                    
                    progress = CourseProgress.query.filter_by(user_id=emp.id).all()
                    print(f"Course assignments: {len(progress)}")
                    for p in progress:
                        print(f"- Course: {p.course.name} (Status: {p.status})")
                
            except Exception as e:
                print(f"Error creating test data: {e}")
                db.session.rollback()
            
    app.run(debug=True) 