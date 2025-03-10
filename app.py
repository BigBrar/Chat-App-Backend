# app.py
from config import create_app, db, socketio
from routes.auth import auth_bp
from routes.chat import chat_bp
from websockets import setup_socketio_events

# Initialize the app
app = create_app()

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(chat_bp, url_prefix='/chat')

# Set up WebSocket events
setup_socketio_events(socketio)

@app.route('/')
def main_function():
    return 'The flask backend is running :)     !!!'

# Main entry point
if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0',port=80,allow_unsafe_werkzeug=True)
