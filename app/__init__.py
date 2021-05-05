from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

# Instatiate flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    ''' Application factory for Flask application '''
    # Initialize app and load in config/environment settings
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    @app.route('/test')
    def test():
        return '<h1>Test</h1>'

    return app