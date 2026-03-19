import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { apiCall } from '../config';
import './Home.css';

function Home() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const data = await apiCall('/');
        setPosts(data.posts || []);
      } catch (error) {
        console.log('Error fetching posts:', error);
        setPosts([]);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  return (
    <div className="home">
      <div className="container">
        <div className="hero">
          <div className="hero-content">
            <h1>Hi, I'm Ayush Pandey</h1>
            <p className="subtitle">A student | Storyteller | Dancer | Singer</p>
            <p className="description">
              I'm a 10th grade student from Silver Grove School, Varanasi, Uttar Pradesh. 
              I love telling stories, dancing, and singing!
            </p>
            <div className="hero-buttons">
              <Link to="/about" className="btn btn-primary">Learn About Me</Link>
              <Link to="/stories" className="btn btn-secondary">Read My Stories</Link>
            </div>
          </div>
          <div className="hero-image">
            <div className="avatar">
              <span>🎓</span>
            </div>
          </div>
        </div>

        <div className="highlights">
          <div className="highlight-card">
            <div className="icon">✍️</div>
            <h3>Storytelling</h3>
            <p>I love creating engaging stories and sharing them with others.</p>
          </div>
          <div className="highlight-card">
            <div className="icon">💃</div>
            <h3>Dancing</h3>
            <p>Dance is my passion and a way to express myself.</p>
          </div>
          <div className="highlight-card">
            <div className="icon">🎤</div>
            <h3>Singing</h3>
            <p>Music and singing bring joy to my life.</p>
          </div>
        </div>

        <div className="recent-posts">
          <h2>Recent Posts</h2>
          {loading ? (
            <p>Loading posts...</p>
          ) : posts.length > 0 ? (
            <div className="posts-grid">
              {posts.map(post => (
                <div key={post.id} className="post-preview">
                  <h3>{post.title}</h3>
                  <p className="post-meta">
                    <span className="author">{post.author}</span>
                    <span className="category">{post.category}</span>
                  </p>
                  <p className="post-date">{new Date(post.created_at).toLocaleDateString()}</p>
                </div>
              ))}
            </div>
          ) : (
            <p>No posts yet. Check back soon!</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default Home;
