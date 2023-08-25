from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

coordinates = {'x': 0, 'y': 0}  # Dicionário para armazenar as coordenadas

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    emit('update_coordinates', coordinates)  # Envia as coordenadas atuais ao cliente

@socketio.on('change_coordinates')  # Evento para receber as coordenadas atualizadas
def change_coordinates(data):
    global coordinates
    coordinates['x'] = data['x']
    coordinates['y'] = data['y']
    emit('update_coordinates', coordinates, broadcast=True)  # Envia as coordenadas atualizadas para todos os clientes

if __name__ == '__main__':
    socketio.run(app, debug=True)
