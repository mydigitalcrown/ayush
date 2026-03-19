from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # Use environment variable for database or fall back to SQLite
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
    
    # Create tables only in development or if needed
    @app.before_request
    def init_db():
        try:
            with app.app_context():
                db.create_all()
        except Exception:
            pass
    
    return app
