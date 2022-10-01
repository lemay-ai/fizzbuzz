
from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse

import uvicorn
import torch
from transformers import AutoFeatureExtractor, ResNetForImageClassification
from PIL import Image

import io


feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

app = Starlette()


@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()

    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)


@app.route("/predict", methods=["POST"])
async def predict(request):
    # if 'media' not in await request.files:
    # return "Please try again. The Image doesn't exist"

    data = await request.form()

    bytes = await (data["media"].read())
    return predict_image_from_bytes(bytes)


def predict_image_from_bytes(bytes):
    # load byte data into a stream
    img_file = io.BytesIO(bytes)
    # encoding the image in base64 to serve in HTML
    img = Image.open(img_file)

    inputs = feature_extractor(img, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits
    # model predicts one of the 1000 ImageNet classes
    predicted_label_1 = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_label_1]

    return JSONResponse({'Prediction': predicted_label})


@app.route("/")
def form(request):
    return HTMLResponse(
        """
            <h1> Image Classification </h1>
            <p> what is the object in the image?? </p>
            <form action="/upload" method = "post" enctype = "multipart/form-data">
                <u> Select picture to upload: </u> <br> <p>
                1. <input type="file" name="file"><br><p>
                2. <input type="submit" value="Upload">
            </form>
            
            """)


@app.route("/form")
def redirect_to_homepage(request):
    return RedirectResponse("/")


if __name__ == "__main__":

    port = 5050
    uvicorn.run(app, host="0.0.0.0", port=port)
