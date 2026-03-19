import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
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
      </div>
    </div>
  );
}

export default Home;
