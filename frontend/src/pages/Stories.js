import React, { useState, useEffect } from 'react';
import { apiCall } from '../config';
import './Stories.css';

function Stories() {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStories = async () => {
      try {
        const data = await apiCall('/api/posts?page=1');
        setStories(data.posts || []);
        setLoading(false);
      } catch (error) {
        console.log('Error fetching stories:', error);
        // Fallback stories
        setStories([
          {
            id: 1,
            title: 'Welcome to Ayush\'s Blog',
            content: 'This is a welcome post about the personal blog of Ayush Pandey.',
            author: 'Ayush Pandey',
            category: 'Welcome',
            created_at: new Date().toISOString()
          }
        ]);
        setLoading(false);
      }
    };

    fetchStories();
  }, []);

  if (loading) {
    return <div className="stories"><p>Loading stories...</p></div>;
  }

  return (
    <div className="stories">
      <div className="container">
        <h1>My Stories</h1>
        <p className="stories-intro">
          Explore my collection of creative stories. I love storytelling and writing about 
          fictional worlds, adventures, and imaginary characters.
        </p>

        <div className="stories-grid">
          {stories.map(story => (
            <div key={story.id} className="story-card">
              <div className="story-header">
                <h2>{story.title}</h2>
                <span className="story-date">{new Date(story.created_at).toLocaleDateString()}</span>
              </div>
              <p className="story-excerpt">{story.content.substring(0, 150)}...</p>
              <button className="read-more-btn">Read More →</button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Stories;
