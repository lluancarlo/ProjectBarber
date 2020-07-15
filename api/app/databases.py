from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_db(app):
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app
