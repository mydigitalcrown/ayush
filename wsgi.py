import os
import sys
import logging
from dotenv import load_dotenv

load_dotenv()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

try:
    logger.info("Starting Flask app initialization...")
    from app import create_app
    app = create_app()
    logger.info("Flask app created successfully!")
except Exception as e:
    logger.error(f"Failed to create Flask app: {e}", exc_info=True)
    # Fallback minimal app
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    def error():
        return jsonify({
            'error': 'Application initialization failed',
            'message': str(e)
        }), 500
    
    @app.route('/health')
    def health():
        return jsonify({
            'error': 'Application initialization failed',
            'message': str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=False)
