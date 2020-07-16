from .index import app as index
from .admin.route.user import app as user

def routes(app):
    # Rotas padrão do sistema.
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(user, url_prefix='/admin/user')