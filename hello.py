from flask import Flask

app = Flask(__name__)

@app.route('/') #este decorador va a hacer que el servidor reconozca esta barra y poder acceder a la ruta
def el_que_nos_de_la_gana():
    return '¡Hola, mundo!'

@app.route('/bye')
def otro():
    return "Adios, mundo cruel!"