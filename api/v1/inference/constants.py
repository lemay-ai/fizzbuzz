"""
File to store all constants for our application
"""


class Constants:
    """
    Constants file to store inference related constants
    """
    ASR_INFERENCE_ENDPOINT = "https://api-inference.huggingface.co/models/facebook/wav2vec2-large-960h-lv60-self"
    DATA_FOLDER = "data/"
    DEFAULT_INFERENCE_FILE_NAME = "84-121550-0000.flac"
    VERSION_V1 = "v1"
    DEFAULT_PORT = 5000
    STATUS_CODE_SUCCESS = 200
    STATUS_CODE_SUCCESS_MESSAGE = "Inference successful"
    STATUS_CODE_INTERNAL_SERVER_ERROR = 500
    STATUS_CODE_INTERNAL_SERVER_ERROR_MESSAGE = "Failure due to internal server error"
    MESSAGE = "message"
    INFERENCE_FAILED = "Inference failed ! "
