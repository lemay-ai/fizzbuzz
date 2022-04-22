from flask import Flask, request, jsonify, render_template
from service import Service

# Create flask app
flask_app = Flask(__name__)

# f = open('txtvetorizador_5.pkl','rb')
# txtvetorizador = pickle.load(f)
# f.close()

# f = open('modelo_5.pkl','rb')
# model = pickle.load(f)
# f.close()

service = Service()


@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/front_predict", methods = ["POST"])
def front_predict():
    features =  request.form['text']
    txtvetorizador, model = service.load_model()
    pred = service.predict(features, txtvetorizador, model)
    return render_template("index.html", prediction_text = "The prediction is {}".format(pred))

@flask_app.route("/endpoint_predict", methods = ["POST"])
def endpoint_predict():
    features =  request.form['text']
    txtvetorizador, model = service.load_model()
    pred = service.predict(features, txtvetorizador, model)
    return pred

if __name__ == "__main__":
    debug = True #means that the page will update automaticaly
    flask_app.run(host = '0.0.0.0', port = 5000, debug = debug)


# @namespace.route('/consulta_intencoes_assertividade_mais_baixa')
# class consulta_intencoes_assertividade_mais_baixa(Resource):
#     @cross_origin(origin=['localhost'],headers=['Content-Type','Authorization'])
#     @namespace.doc('consulta_intencoes_assertividade_mais_baixa')
#     @namespace.response(200, "Busca realizada com sucesso")