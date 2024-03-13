from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_socketio import SocketIO

from config import Config
from flask_cors import CORS

class Events:
    def __init__(self):
        self.app = Flask(__name__)
        
        CORS(self.app,resources={r"//*": {"origins": "http://localhost:8000"}})
        self.socketio = SocketIO(self.app,cors_allowed_origins="*")
        
        bootstrap = Bootstrap5(self.app)
        self.app.config['SECRET_KEY'] = Config().secret_app
        @self.socketio.on('message')
        def handle_message(data):
            print('received message d: ' + str(data))
        
        
        
    def runner(self):
        self.socketio.run(app=self.app,host=Config().host, port=3000,
                     debug=Config().debu)

def run_app():
    aplication = Events()
    return aplication.socketio
if __name__ == '__main__':
    aplication = Events()
    aplication.runner()