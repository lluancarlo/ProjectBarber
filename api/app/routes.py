from .index import app as index


def routes(app):
    # Rotas padrão do sistema.
    app.register_blueprint(index, url_prefix='/')