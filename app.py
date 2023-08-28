from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

coordinates = {'x': 0, 'y': 0}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    emit('update_coordinates', coordinates)

@socketio.on('change_coordinates')
def change_coordinates(data):
    global coordinates
    coordinates['xMax'] = data['xMax']
    coordinates['xMin'] = data['xMin']
    coordinates['yMax'] = data['yMax']
    coordinates['yMin'] = data['yMin']
    coordinates['x'] = data['xMax'] - data['xMin']
    coordinates['y'] = data['yMax'] - data['yMin']

    emit('update_coordinates', coordinates, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
