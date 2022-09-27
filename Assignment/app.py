import io
import numpy as np
import torch
from flask import Flask, jsonify, request
from transformers import AutoFeatureExtractor, ResNetForImageClassification
from PIL import Image




feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer_image():  
    
    if 'media' not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files['media']

    if not file:
        return
    
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))

    inputs = feature_extractor(img, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits
# model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    return jsonify(model.config.id2label[predicted_label])

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




