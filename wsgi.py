import os
from dotenv import load_dotenv

load_dotenv()

try:
    from app import create_app
    app = create_app()
except Exception as e:
    # If app creation fails, create a minimal Flask app for error response
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    def error():
        return jsonify({'error': 'Application failed to initialize', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run()
