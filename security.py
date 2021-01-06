from werkzeug.security import safe_str_cmp
from models.user import User


def authenticate(username, password):

    user = User.return_users_logged(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):

    user_id = payload['identity']
    return User.return_users_id(user_id)
