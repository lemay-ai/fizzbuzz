from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from redis import Redis
from rq import Queue

app = Flask(__name__, template_folder = "../templates")
app.config.from_object(Config)
db = SQLAlchemy(app)
app.redis = Redis.from_url(app.config['REDIS_URL'])
app.task_queue = Queue('msg_tasks', connection=app.redis)
migrate = Migrate(app, db)

from app import routes, models