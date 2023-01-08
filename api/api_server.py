"""
This is the api server application to start our inference application
"""

from flask import Flask, Blueprint
from flask_restx import Api

from v1.inference.app import inference_ns

app = Flask(__name__)
bp = Blueprint('api', __name__)
app.register_blueprint(bp)
api = Api(app)
api.add_namespace(inference_ns, path="/api/v1/inference")


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, threaded=True)
