from flask import Flask,jsonify,request
from flask_cors import CORS
from datetime import datetime
#biblioteca adicional a las de calse
from collections import OrderedDict
import logging
#inicia flask
app =Flask(__name__)
#permite comunicacion entre puetos
CORS(app)
#kwargs
tipo_medicion ={'sensor':'DHT11','variable':'humedad','unidades': '%' }

mediciones =[
    {'fecha': '2019-08-10 11:24:08',**tipo_medicion,'valor':0.85},
    {'fecha': '2019-08-11 13:24:08',**tipo_medicion,'valor':0.75},
    {'fecha': '2019-08-12 12:24:08',**tipo_medicion,'valor':0.6},
    {'fecha': '2019-08-13 10:24:08',**tipo_medicion,'valor':0.73},
    {'fecha': '2019-08-14 13:24:08',**tipo_medicion,'valor':0.71},
    {'fecha': '2019-08-15 08:24:08',**tipo_medicion,'valor':0.67},
    {'fecha': '2019-08-16 09:24:08',**tipo_medicion,'valor':0.72}
]
@app.route('/')
def get():
    return jsonify (tipo_medicion)

@app.route('/todo')
def getA():
    return jsonify(mediciones)
        
@app.route('/mediciones',methods=['POST'])
def postOne():
    now = datetime.now()
    body = request.json
    body['fecha']=datetime.strftime(now,'%Y-%m-%d %H:-%M-%S')
    mediciones.append({**body,**tipo_medicion})
    return jsonify(mediciones)
@app.route('/top30%')
def topMed():
    #top = mediciones.sort(valor,reverse =True)
    total = len(mediciones)
    mostrar = int(total*0.30) 
    top = sorted(mediciones, key = lambda i: i['valor'], reverse= True)
    #top = mediciones.sort(mediciones[])
    while len(top) > mostrar:
        top.pop()
        
    return jsonify(top)

# @app.route('/mediciones/fecha/<string:fecha>',methods=['GET'])
# def getbyFecha(fecha):

app.run(port=5555,debug=True)
    
