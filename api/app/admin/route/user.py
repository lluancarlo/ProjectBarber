"""
Rotas para o modulo User.
"""

from flask import jsonify

from ...admin.modules.user import Users
from ...app_json import AppBlueprint
from ...helpers.response import response_wrapper_success

"""Blueprint para registrar a rota de user.
"""
app = AppBlueprint('admin.user', __name__)

USERS = Users()


@app.route('<doc_id>', methods=['GET'])
def get(doc_id):
    """Retorna o usuário cadastrado no sistema"""
    return dict() 


@app.route('', methods=['POST'])
def create():
    """Inicia o processo de cadastro de um novo usuário"""
    return dict()    