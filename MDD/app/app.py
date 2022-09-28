import os
import traceback
from transformers import AutoFeatureExtractor, ResNetForImageClassification
import torch
from flask import Flask, jsonify, request
from PIL import Image

class WebApp():

    def __init__(self, app):
        self.app = app


    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['POST'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    def load_model(self):
        
        model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
        return model

    def init_feature(self):
        feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-50")
        return feature_extractor

                 
         
    def predict(self):
        json = request.get_json()
        image_name = json['image name']
        image_path = os.path.join('data', image_name)
        if not os.path.exists(image_path):
            return "Image Does Not Exist"
        image = Image.open(image_path)
        if len(image.size) == 2:
            image = image.convert('RGB')
        feature_extractor = self.init_feature()
        model = self.load_model()

        inputs = feature_extractor(image, return_tensors="pt")

        with torch.no_grad():
            logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
        predicted_label = logits.argmax(-1).item()
        print(model.config.id2label[predicted_label])

        return model.config.id2label[predicted_label]

    
    def handle_exception(e):
        return jsonify(stackTrace=traceback.format_exc())

flask_app = Flask(__name__)

app = WebApp(flask_app)

app.add_endpoint('/predict', 'predict', app.predict, methods=['POST'])

if __name__== "__main__":
    app.run('localhost', 5000)
