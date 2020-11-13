from app import db
from app.models import Msg
import datetime
import json
import requests as reqs
from sqlalchemy import func
from functools import wraps

##export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {}".format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer
def db_insert(data, arrival_time):
    try:
        msg = json.loads(data)["msg_num"]
        delivery_time = arrival_time - datetime.datetime\
            .strptime(json.loads(data)["start"], '%Y-%m-%d %H:%M:%S.%f')
        delivery_time = float(delivery_time.microseconds / 1000)
        msg = Msg(msg_num = msg, time = delivery_time)
        db.session.add(msg)
        db.session.commit()
    except:
        raise Exception("something went wrong!")