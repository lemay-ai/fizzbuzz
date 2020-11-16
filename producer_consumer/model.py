from app import app, db
from app.models import Msg

def make_shell_context():
    return {'db': db, 'Msg': Msg}
