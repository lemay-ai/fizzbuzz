from fastapi import FastAPI, Form
from pydantic import BaseModel
from transformers import pipeline, set_seed


app = FastAPI()
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

class PostData(BaseModel):
	topic: str
	max_length: int

@app.get('/')
def index():
	return {'note': 'Please use the following path urls for documentation and testing the model',
			'url': '/compare',
			'doc': '/docs'}


@app.post('/compare')
def compare(data:PostData):
	try:
		text = generator(data.topic, max_length=data.max_length, num_return_sequences=1)
		return {'text': text[0]['generated_text']}
	except Exception as e:
		print(e)
		return {'text': 'Something went wrong 🤯'}
