from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logging

db = SQLAlchemy()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # Database configuration
    if os.environ.get('DATABASE_URL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    else:
        # SQLite for development
        db_path = os.path.join(os.path.dirname(__file__), 'blog.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    from app.routes import main_bp, blog_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp)
    
    # Context for database operations
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            logger.warning(f"Could not create database tables: {e}")
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def server_error(e):
        logger.error(f"Server error: {e}")
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500
    
    return app
