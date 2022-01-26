from flask import Flask,render_template,request
from transformers import pipeline
 
app = Flask(__name__)
 
@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        text_generate = pipeline("text-generation")
        print(request.form)
        generated_txt = text_generate(request.form["Name"], max_length = 50, do_sample=False)[0]
        print('--------------------', generated_txt['generated_text'])
        #form_data = {"output":generated_txt["generated_txt"]}
        #print(type(generated_txt['generated_txt'])
        return render_template('data.html', form_data = generated_txt['generated_text'])  
        
app.run(host='localhost', port=5000, debug = False)
