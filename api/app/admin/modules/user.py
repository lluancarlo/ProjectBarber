"""
Controller User.
"""
from datetime import timedelta, datetime

from app.databases import db
from app.helpers.datetime_helpers import now
from app.models.user_model import User


class Users:
    def get(self, id):
        return 'o id do user eh: ' + id

    def create(self, data):
        if not data:
            return 'error 409'
        user = User(data.get('name'),
                    data.get('username'),
                    data.get('email')
        )

        db.session.add(user)
        db.session.commit()

        return 'criado com sucesso'

