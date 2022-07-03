from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path
import logging

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})

    app.config['SECRET_KEY'] = 'uc328b3787dsa'

    from .views import views
    app.register_blueprint(views, url_prefix='/api')

    return app

class Response(dict):
    def __init__(self, status, body):
        super().__init__(self, status=status, body=body)
