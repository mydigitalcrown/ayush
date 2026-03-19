from flask import Blueprint, jsonify, request
from app import db
from app.models import Post, Comment
from datetime import datetime

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
        return jsonify({'error': str(e), 'status': 'error'}), 500

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
        return jsonify({'error': str(e)}), 500

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
        return jsonify({'error': str(e)}), 500

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
        return jsonify({'error': str(e)}), 404

@blog_bp.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        
        data = request.get_json()
        author = data.get('author', '')
        email = data.get('email', '')
        content = data.get('content', '')
        
        if author and email and content:
            comment = Comment(author=author, email=email, content=content, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Comment added'}), 201
        else:
            return jsonify({'error': 'Missing required fields'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        flash('All fields are required!', 'error')
    
    return redirect(url_for('blog.view_post', post_id=post_id))

@blog_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        author = request.form.get('author', 'Admin')
        category = request.form.get('category', 'General')
        
        if title and content:
            post = Post(title=title, content=content, author=author, category=category)
            db.session.add(post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('blog.view_post', post_id=post.id))
        else:
            flash('Title and content are required!', 'error')
    
    return render_template('blog/create.html')

@blog_bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        post.title = request.form.get('title', post.title)
        post.content = request.form.get('content', post.content)
        post.author = request.form.get('author', post.author)
        post.category = request.form.get('category', post.category)
        post.updated_at = datetime.utcnow()
        
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('blog.view_post', post_id=post.id))
    
    return render_template('blog/edit.html', post=post)

@blog_bp.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    # Delete associated comments
    Comment.query.filter_by(post_id=post_id).delete()
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('blog.list_posts'))
