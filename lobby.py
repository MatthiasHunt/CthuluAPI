from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config.from_pyfile('config.py')
socketio = SocketIO(app)

@app.route('/')
def basicTemplate():
    return render_template('sample.html') #This is placeholder front-end

def messageReceived():
    print('Message was received')
    return True

@socketio.on('message')
def echo(str):
    emit('test event', str, callback=messageReceived)

if __name__ == "__main__":
    socketio.run(app)