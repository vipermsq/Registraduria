from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi
app = Flask(__name__)
cors = CORS(app)


from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()

from Controladores.ControladorMesa import ControladorMesa
miControladorMesa = ControladorMesa()

from Controladores.ControladorPartido import ControladorPartido
miControladorPartido = ControladorPartido()

from Controladores.ControladorResultado import ControladorResultado
miControladorResultado = ControladorResultado()





## rutas para Candidatos

@app.route("/candidatos", methods=['GET'])
def indexCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def createCandidatos():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def updateCandidatos(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def deleteCandidatos(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def showCandidatos(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partido/<string:id_partido>", methods=['PUT'])
def setPartidoCandidatos(id_candidato, id_partido):
    json = miControladorCandidato.setPartido(id_candidato, id_partido)
    return jsonify(json)


## rutas para Mesa

@app.route("/mesas", methods=['GET'])
def indexMesa():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=['POST'])
def createMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def updateMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def deleteMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def showMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

## rutas para Partido

@app.route("/partidos", methods=['GET'])
def indexPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def createPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def updatePartidos(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def deletePartidos(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def showPartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

# Rutas de RESULTADOS
@app.route("/resultados", methods=['GET'])
def indexResultados():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def createResultados(id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.create(data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def updateResultados(id_resultado, id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def deleteResultados(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def showResultados(id):
    json = miControladorResultado.show(id)
    return jsonify(json)
############################################################

def loadConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    ca = certifi.where()
    client = pymongo.MongoClient(
        "mongodb+srv://admin:MongoDb12345$@cluster0.7xdinwa.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFILE=ca)
    db = client.test
    print(db)
    baseDatos = client['RegistraduriaMSQ']
    print(baseDatos.list_collection_names())

    dataConfig = loadConfig()
    print("Servicio corriendo......." + "http://" + dataConfig['url-backend'] + ":"+str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
