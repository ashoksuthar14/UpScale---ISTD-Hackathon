from flask import Blueprint

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__, url_prefix='/auth')
manager = Blueprint('manager', __name__, url_prefix='/manager')
employee = Blueprint('employee', __name__, url_prefix='/employee')

from app.routes import main_routes, auth_routes, manager_routes, employee_routes 