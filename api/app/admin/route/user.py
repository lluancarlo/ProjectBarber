"""
Rotas para o modulo User.
"""

from flask import jsonify, request

from ...admin.modules.user import Users
from ...app_json import AppBlueprint
from ...helpers.response import response_wrapper_success, response_wrapper
from flask import make_response

"""Blueprint para registrar a rota de user.
"""
app = AppBlueprint('admin.user', __name__)

USER = Users()


@app.route('<doc_id>', methods=['GET'])
def get_by_id(doc_id):
    """Retorna o usuário cadastrado no sistema"""
    if request.method == "GET":
        find = USER.get_by_id(doc_id)
    if find == None:
            return make_response('Nenhum usuario encontrado com esse ID')    
    return make_response(f'{find.username} Encontrado')


@app.route('', methods=['GET'])
def get():
    """Retorna o usuário cadastrado no sistema"""
    if request.method == "GET":
        find = USER.get()
    if not find:
            return make_response('Nenhum usuario encontrado')
    return make_response(f'{find} Encontrado')

@app.route('', methods=["POST"])
def create():
    """Cadastra o usuário no sistema"""
    if request.method == "POST":
        created = USER.create(data=request.json)
    return make_response("Usuario criado com sucesso!")


@app.route('<doc_id>', methods=["DELETE"])
def delete(doc_id):
    """Deleta o usuário do banco"""
    if request.method == "DELETE":
        delete = USER.delete(id=doc_id)
    return make_response('Usuario deletado com sucesso!')


@app.route('<doc_id>', methods=["PUT"])
def update(doc_id):
    """Altera o usuário do banco"""
    if request.method == "PUT":
        updated = USER.update(id=doc_id, data=request.json)
    return make_response(f'Usuario {updated} alterado com sucesso!')
