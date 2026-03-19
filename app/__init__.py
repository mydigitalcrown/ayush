from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    # Get absolute base directory
    basedir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(basedir)
    
    app = Flask(__name__, 
                template_folder=os.path.join(parent_dir, 'app', 'templates'),
                static_folder=os.path.join(parent_dir, 'app', 'static'))
    
    # Configuration
    if os.environ.get('DATABASE_URL'):
        database_url = os.environ.get('DATABASE_URL')
    else:
        database_url = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-this')
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    try:
        from app.routes import main_bp, blog_bp
        app.register_blueprint(main_bp)
        app.register_blueprint(blog_bp)
    except Exception as e:
        app.logger.error(f"Error registering blueprints: {e}")
        # Add a fallback route
        @app.route('/')
        def fallback():
            from flask import jsonify
            return jsonify({'error': str(e), 'status': 'App partially loaded'}), 500
    
    # Create tables with error handling
    @app.before_request
    def init_db():
        try:
            with app.app_context():
                db.create_all()
        except Exception as e:
            app.logger.warning(f"Warning: Could not create database tables: {e}")
    
    # Global error handler
    @app.errorhandler(404)
    def not_found(e):
        from flask import jsonify
        return jsonify({'error': 'Not found', 'message': 'Endpoint does not exist'}), 404
    
    @app.errorhandler(500)
    def server_error(e):
        from flask import jsonify
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    
    return app
