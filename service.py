import pickle
import numpy as np
import pandas as pd
import string

class Service():

    def load_model(self):
        f = open('txtvetorizador_5.pkl','rb')
        txtvetorizador = pickle.load(f)
        f.close()

        f = open('modelo_5.pkl','rb')
        model = pickle.load(f)
        f.close()

        return txtvetorizador, model

    def predict(self, features, txtvetorizador, model):
        lista = []
        lista.append(features)
        novoVetor = txtvetorizador.transform(lista)
        pred = model.predict(novoVetor)
        return np.array2string(pred[-1])

