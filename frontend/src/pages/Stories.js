import React, { useState, useEffect } from 'react';
import './Stories.css';

function Stories() {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:5000/api/stories')
      .then(res => res.json())
      .then(data => {
        setStories(data);
        setLoading(false);
      })
      .catch(err => {
        console.log('Error:', err);
        setLoading(false);
      });
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
                <span className="story-date">{new Date(story.date).toLocaleDateString()}</span>
              </div>
              <p className="story-excerpt">{story.excerpt}</p>
              <button className="read-more-btn">Read More →</button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Stories;
