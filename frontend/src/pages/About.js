import React, { useState, useEffect } from 'react';
import './About.css';

function About() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/about')
      .then(res => res.json())
      .then(data => setProfile(data))
      .catch(err => console.log('Error:', err));
  }, []);

  if (!profile) {
    return <div className="about"><p>Loading...</p></div>;
  }

  return (
    <div className="about">
      <div className="container">
        <h1>About Me</h1>
        
        <div className="about-content">
          <div className="about-text">
            <div className="info-card">
              <h2>Personal Information</h2>
              <ul>
                <li><strong>Name:</strong> {profile.name}</li>
                <li><strong>Grade:</strong> {profile.class}</li>
                <li><strong>School:</strong> {profile.school}</li>
                <li><strong>Location:</strong> {profile.location}</li>
              </ul>
            </div>

            <div className="info-card">
              <h2>My Hobbies</h2>
              <ul className="hobbies-list">
                {profile.hobbies.map((hobby, idx) => (
                  <li key={idx}>🎉 {hobby}</li>
                ))}
              </ul>
            </div>

            <div className="info-card">
              <h2>My Talent</h2>
              <p className="talent-text">
                <strong>✨ {profile.talent}</strong>
              </p>
              <p>
                I love creating fictional worlds and stories. Writing helps me express my creativity 
                and imagination. I enjoy crafting engaging narratives that captivate readers.
              </p>
            </div>
          </div>

          <div className="about-image">
            <div className="image-placeholder">
              <span>📚</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
