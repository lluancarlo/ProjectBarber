"""Rota para index
"""
from flask import Blueprint

app = Blueprint('index', __name__)


@app.route('/nrping', methods=['GET'])
def ping():
    return dict(
        buildDate="dd/mm/yyyy",
        version="1.0"
    )