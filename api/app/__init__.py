"""inicia o flask app."""
from flask import Flask

from .databases import config_db
from .routes import routes


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    config_db(app)

    routes(app)

    return app