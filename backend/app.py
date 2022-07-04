""" create flask app for local testing """

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})

    app.config['SECRET_KEY'] = 'uc328b3787dsa'

    from views import views
    app.register_blueprint(views, url_prefix='/api')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
