import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'model'),
        os.getenv('DB_PASSWORD', 'slimdingo85'),
        os.getenv('DB_HOST', 'mysql'),
        os.getenv('DB_NAME', 'model')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False








