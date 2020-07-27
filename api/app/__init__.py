"""inicia o flask app."""
from flask import Flask

from .config import Config
from .databases import config_db
from .routes import routes

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config())

    config_db(app)
    routes(app)

    return app
