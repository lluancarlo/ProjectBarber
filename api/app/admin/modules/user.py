"""
Controller User.
"""
from datetime import timedelta, datetime
from flask import make_response


from ...databases import db
from ...helpers.datetime_helpers import now
from ...helpers.response import response_wrapper, response_wrapper_error, response_wrapper_success
from ...models.user_model import User
from ...schemas.user_schema import UserSchema

user_schema = UserSchema()


class Users:
    def get_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user    
    

    def create(self, data):
        if not data:
            return response_wrapper_error(code='409', message='Envie as informações corretas', data=data), 409

        user = User(data.get('username'), data.get('email'))

        db.session.add(user)
        db.session.commit()

        if user == None:
            return response_wrapper_error(code='409', message='Usuario não foi criado', data=data), 409

        return user    


    def delete(self, id):
        user = User.query.filter_by(id=id).first()

        db.session.delete(user)
        db.session.commit()


    def update(self, id, data):
        user = User.query.filter_by(id=id).first()
       
        if not data:
            return response_wrapper_error(code='409', message='Envie as informações necessarias', data=None), 409

        user.username = data.get('username')
        user.email = data.get('email')

        db.session.commit()

        return data    
    

