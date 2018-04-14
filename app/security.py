from flask_jwt import JWT

from .models import User


def authentication_handler(username, password) -> User:
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


def identity_handler(payload):
    user_id = payload['identity']
    return User.query.get(user_id)


jwt = JWT(authentication_handler=authentication_handler,
          identity_handler=identity_handler)
