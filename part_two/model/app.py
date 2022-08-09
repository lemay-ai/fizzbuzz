from flask import Flask, request, jsonify, render_template
import pickle

import requests

API_TOKEN = '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'

API_URL = "https://api-inference.huggingface.co/models/Zixtrauce/BaekBot"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
past_user_inputs = []
generated_responses = []
last_user_input = ""

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat',methods=['POST'])
def chat():
    '''
    For rendering results on HTML GUI
    '''

    features = request.form.to_dict()
    text = features['user']

    unrenderd_output = query({
	"inputs": {
            "past_user_inputs": past_user_inputs,
            "generated_responses": generated_responses,
            "text": text
	    },
    })

    output = unrenderd_output['generated_text']

    past_user_inputs.insert(0, text)
    if (len(past_user_inputs)>2):
        past_user_inputs.pop()
    generated_responses.insert(0, output)
    if(len(generated_responses)>2):
        generated_responses.pop()

    return render_template('index.html', prediction_text='BaekBot: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')