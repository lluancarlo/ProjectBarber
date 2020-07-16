"""
Rotas para o modulo User.
"""

from flask import jsonify, request

from ...admin.modules.user import Users
from ...app_json import AppBlueprint
from ...helpers.response import response_wrapper_success, response_wrapper

"""Blueprint para registrar a rota de user.
"""
app = AppBlueprint('admin.user', __name__)

USER = Users()


@app.route('<id>', methods=['GET'])
def get(id):
    """Retorna o usuário cadastrado no sistema"""
    find = USER.get(id)
    return find


@app.route('', methods=["POST"])
def contact_request():
    """Cadastra o usuário no sistema"""
    if request.method == "POST":
        created = USER.create(data=request.json)
    return created
