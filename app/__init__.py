from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-change-this'
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    from app.routes import main_bp, blog_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
