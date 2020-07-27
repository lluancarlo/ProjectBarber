from ..databases import ma
from ..models.user_model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    email = ma.auto_field()
    username = ma.auto_field()
