
import pickle
from fastapi import FastAPI
from transformers import pipeline
import uvicorn

app = FastAPI()

pickle.dump(pipeline('sentiment-analysis'), open('./model/model.pkl', 'wb'))
classifier = pickle.load(open('./model/model.pkl', 'rb'))

@app.get("/")
async def read_root():
    return {"text": "tweet Sentiment analysis"}


@app.post("/state_analysis/{text}")
async def state_analysis(text):
    # Get values from browser
    #classifier = pipeline('sentiment-analysis')

    return classifier(text)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)
