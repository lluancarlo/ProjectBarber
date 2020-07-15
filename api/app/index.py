"""Rota para index
"""
from flask import Blueprint

app = Blueprint('index', __name__)

@app.route('/index', methods=['GET'])
def ping():
    return dict(
        message="Hello Word",  
        status="200"  
        )

