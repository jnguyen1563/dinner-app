import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    @app.route('/test')
    def test():
        return '<h1>Test</h1>'

    return app