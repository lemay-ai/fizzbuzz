# import objects from the Flask model
from flask import Flask, jsonify, render_template, request, make_response
import transformers
import socket

# creating flask app
app = Flask(__name__)

pretrained_model = transformers.pipeline('sentiment-analysis', model ="finiteautomata/bertweet-base-sentiment-analysis")

# inference fonction
def get_prediction(message,model):
    # inference
    results = model(message)  
    return results

# get method
@app.route('/', methods=['GET'])
def get():
    # in the select we will have each key of the list in option
    return render_template("home.html")


# post method
@app.route('/', methods=['POST'])
def predict():
    message = request.form['message']
    
    # choice of the model
    results = get_prediction(message, pretrained_model)
    print("Model Used here is BERT")
    my_prediction = f'The sentiment of this text is : {results[0]["label"]} with a Probabilty Score :  {round(results[0]["score"], 2)*100} %.'
 
    return render_template('result.html', text = f'{message}', prediction = my_prediction)


print(f"socket = {socket.gethostname()}")

if __name__ == '__main__':
    # starting app
    app.run(debug=True,host='0.0.0.0')