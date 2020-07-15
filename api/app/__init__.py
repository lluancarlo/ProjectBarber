"""inicia o flask app."""
import logging
from flask import Flask
import re
from pathlib import Path

from flask import request

from .databases import config_db
from .helpers.json import sanetize_request
from .routes import routes


def create_app():
    app = Flask(__name__)

    config_db(app)

    routes(app)
    return app

    @app.before_request
    def before_request_func():
        sanetize_request(request.get_json())

    @app.after_request
    def after_request_func(response):
        return response
