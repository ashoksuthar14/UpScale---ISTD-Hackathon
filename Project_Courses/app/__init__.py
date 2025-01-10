from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)

    from app.routes import main, auth, manager, employee
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(manager)
    app.register_blueprint(employee)

    return app 