"""
Controller User.
"""
from datetime import timedelta, datetime


from app.databases import db
from app.helpers.datetime_helpers import now
from app.models.user_model import User
from flask import make_response


class Users:
    def get_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user    
    

    def get(self):
        user = User.query.all()

        result = [r.username for r in user]
        return result

    def create(self, data):
        if not data:
            return 'error 409'
        user = User(data.get('username'), data.get('email'))

        db.session.add(user)
        db.session.commit()

        if user == None:
            return 'Error 409'


    def delete(self, id):
        if not id:
            return 'error'

        user = User.query.filter_by(id=id).first()

        if user == None:
            return make_response('Usuario não encontrado')

        db.session.delete(user)
        db.session.commit()

    def update(self, id, data):
        user = User.query.filter_by(id=id).first()

        if not data or not user:
            return 'error 409'
       
        user.username = data.get('username')
        user.email = data.get('email')

        db.session.commit()

        return user.username    
    

