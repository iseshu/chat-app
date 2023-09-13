from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
Socket = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@Socket.on('message')
def handle_message(data):
    print('received message: ' + data)
    if data != "User Connected":
        send(data, broadcast=True)

if __name__ == '__main__':
    Socket.run(app)