"""
Rotas para o modulo User.
"""

from flask import jsonify, request, make_response


from ...admin.modules.user import Users
from ...app_json import AppBlueprint
from ...helpers.response import response_wrapper_success, response_wrapper, response_wrapper_error
from ...schemas.user_schema import UserSchema

"""Blueprint para registrar a rota de user.
"""
app = AppBlueprint('admin.user', __name__)

USER = Users()
user_schema = UserSchema()


@app.route('<id>', methods=['GET'])
def get_by_id(id):
    """Retorna o usuário cadastrado no sistema"""
    if request.method == "GET":
        find = USER.get_by_id(id)
        if find == None:
            return response_wrapper_error(code='404', message='Não encontrado', data=None), 404
    return response_wrapper_success(message='Usuario encontrado', data=user_schema.dump(find)), 200


@app.route('', methods=["POST"])
def create():
    """Cadastra o usuário no sistema"""
    if request.method == "POST":
        created = USER.create(data=request.json)
    return response_wrapper_success(message='Usuario criado com sucesso!', data=user_schema.dump(created)), 200


@app.route('<id>', methods=["DELETE"])
def delete(id):
    """Deleta o usuário do banco"""
    if request.method == "DELETE":
        delete = USER.delete(id=id)
    return response_wrapper_success(message='Usuario Deletado com sucesso!', data=user_schema.dump(delete)), 200


@app.route('<id>', methods=["PUT"])
def update(id):
    """Altera o usuário do banco"""
    if request.method == "PUT":
        updated = USER.update(id=id, data=request.json)
    return response_wrapper_success(message='Usuario Alterado com sucesso!', data=user_schema.dump(updated)), 200
