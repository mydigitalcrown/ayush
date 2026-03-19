import React from 'react';
import { blogPosts } from '../config';
import './Stories.css';

function Stories() {
  return (
    <div className="stories">
      <div className="container">
        <h1>My Stories</h1>
        <p className="stories-intro">
          Explore my collection of creative stories. I love storytelling and writing about 
          fictional worlds, adventures, and imaginary characters.
        </p>

        <div className="stories-grid">
          {blogPosts.map(story => (
            <div key={story.id} className="story-card">
              <div className="story-header">
                <h2>{story.title}</h2>
                <span className="story-date">{new Date(story.created_at).toLocaleDateString()}</span>
              </div>
              <p className="story-excerpt">{story.content}</p>
              <div className="story-footer">
                <span className="story-author">By {story.author}</span>
                <span className="story-category">{story.category}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Stories;
