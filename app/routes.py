from flask import Blueprint, jsonify, request
from app import db
from app.models import Post, Comment
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)
blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

# Health Check
@main_bp.route('/health')
def health():
    return jsonify({'status': 'ok', 'message': 'App is running'}), 200

# Home Page
@main_bp.route('/')
def index():
    try:
        posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
        return jsonify({
            'status': 'ok',
            'message': 'Welcome to Ayush Pandey\'s Blog',
            'posts': [
                {
                    'id': p.id,
                    'title': p.title,
                    'author': p.author,
                    'category': p.category,
                    'created_at': p.created_at.isoformat()
                } for p in posts
            ]
        }), 200
    except Exception as e:
        logger.warning(f"Database error in index: {e}")
        # Fallback response
        return jsonify({
            'status': 'ok',
            'message': 'Welcome to Ayush Pandey\'s Blog',
            'posts': [
                {
                    'id': 1,
                    'title': 'Welcome to Ayush\'s Blog',
                    'author': 'Ayush Pandey',
                    'category': 'Welcome',
                    'created_at': datetime.now().isoformat()
                }
            ]
        }), 200

@main_bp.route('/about')
def about():
    return jsonify({
        'name': 'Ayush Pandey',
        'class': '10th',
        'school': 'Silver Grove School',
        'location': 'Varanasi, Uttar Pradesh',
        'hobbies': ['Dance', 'Singing'],
        'talent': 'Writing Stories',
        'status': 'ok'
    }), 200

# API endpoint for all posts
@main_bp.route('/api/posts')
def api_posts():
    try:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
        return jsonify({
            'posts': [
                {
                    'id': p.id,
                    'title': p.title,
                    'content': p.content[:200],
                    'author': p.author,
                    'category': p.category,
                    'created_at': p.created_at.isoformat()
                } for p in posts.items
            ],
            'pages': posts.pages,
            'current_page': page
        }), 200
    except Exception as e:
        logger.warning(f"Database error in api_posts: {e}")
        # Fallback response
        return jsonify({
            'posts': [
                {
                    'id': 1,
                    'title': 'Welcome to Ayush\'s Blog',
                    'content': 'This is a welcome post about the blog.',
                    'author': 'Ayush Pandey',
                    'category': 'Welcome',
                    'created_at': datetime.now().isoformat()
                }
            ],
            'pages': 1,
            'current_page': 1
        }), 200

# Blog Routes
@blog_bp.route('/')
def list_posts():
    try:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
        return jsonify({
            'posts': [
                {
                    'id': p.id,
                    'title': p.title,
                    'author': p.author,
                    'category': p.category,
                    'created_at': p.created_at.isoformat()
                } for p in posts.items
            ],
            'pages': posts.pages,
            'current_page': page
        }), 200
    except Exception as e:
        logger.warning(f"Database error in list_posts: {e}")
        # Fallback response
        return jsonify({
            'posts': [],
            'pages': 0,
            'current_page': 1,
            'note': 'Database temporarily unavailable'
        }), 200

@blog_bp.route('/post/<int:post_id>')
def view_post(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
        return jsonify({
            'post': {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': post.author,
                'category': post.category,
                'created_at': post.created_at.isoformat()
            },
            'comments': [
                {
                    'id': c.id,
                    'author': c.author,
                    'content': c.content,
                    'created_at': c.created_at.isoformat()
                } for c in comments
            ]
        }), 200
    except Exception as e:
        logger.warning(f"Database error in view_post: {e}")
        return jsonify({'error': str(e)}), 404

@blog_bp.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    try:
        data = request.get_json()
        author = data.get('author', '')
        email = data.get('email', '')
        content = data.get('content', '')
        
        if author and email and content:
            post = Post.query.get_or_404(post_id)
            comment = Comment(author=author, email=email, content=content, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Comment added'}), 201
        else:
            return jsonify({'error': 'Missing required fields'}), 400
    except Exception as e:
        logger.warning(f"Error adding comment: {e}")
        return jsonify({'error': str(e)}), 500

