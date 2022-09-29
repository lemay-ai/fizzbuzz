from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('In hello world')
    return 'Web App with Python Flask!'

app.run(host="localhost", port=5000)