# Inference API for Facebook Automatic Speech Recognition
import os
from .constants import Constants as CONST
from flask_restx import Resource, Namespace
import requests
import json
# from werkzeug.datastructures import FileStorage

inference_ns = Namespace("Inference", description="Hugging Face Inference endpoint")
parser = inference_ns.parser()
parser.add_argument('filename', required=False, help='File to use for inference')


@inference_ns.route("/")
class Inference(Resource):
    @inference_ns.doc(description="Performs Inference of a provided data file on Hugging Face ASR model")
    @inference_ns.response(CONST.STATUS_CODE_SUCCESS, CONST.STATUS_CODE_SUCCESS_MESSAGE)
    @inference_ns.response(CONST.STATUS_CODE_INTERNAL_SERVER_ERROR, CONST.STATUS_CODE_INTERNAL_SERVER_ERROR_MESSAGE)
    @inference_ns.expect(parser, validate=True)
    def post(self, **kwargs):
        try:
            args = parser.parse_args()
            file_name = args["filename"]
            file_name = "/v1/data/sample/" + file_name
            API_URL = CONST.ASR_INFERENCE_ENDPOINT
            headers = {"Authorization": f"Bearer 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"}
            with open(os.getcwd() + file_name, "rb") as f:
                f.seek(0)
                data = f.read()
            response = requests.request("POST", API_URL, headers=headers, data=data)
            response_object = dict()
            response_object["message"] = json.loads(response.content.decode("utf-8"))
            return response_object, CONST.STATUS_CODE_SUCCESS
        except Exception as e:
            response_object = dict()
            response_object[CONST.MESSAGE] = CONST.INFERENCE_FAILED + str(e)
            return response_object, CONST.STATUS_CODE_INTERNAL_SERVER_ERROR
