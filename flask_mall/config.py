import random
import string


def random_string(length):
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_str


class Config(object):
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql://root:nirvana~@127.0.0.1/flask'
    SECRET_KEY = random_string(20)
