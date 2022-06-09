from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path
import logging

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config['SECRET_KEY'] = 'uc328b3787dsa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/api')

    create_database(app)

    return app


def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        logging.info('Created Database!')
