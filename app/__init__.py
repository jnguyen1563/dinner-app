import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def create_app():
    # Initialize app and load in config/environment settings
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    # 
    db = SQLAlchemy()
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @app.route('/test')
    def test():
        return '<h1>Test</h1>'

    return app