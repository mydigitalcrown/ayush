import React from 'react';
import { profileData } from '../config';
import './About.css';

function About() {
  return (
    <div className="about">
      <div className="container">
        <h1>About Me</h1>
        
        <div className="about-content">
          <div className="about-text">
            <div className="info-card">
              <h2>Personal Information</h2>
              <ul>
                <li><strong>Name:</strong> {profileData.name}</li>
                <li><strong>Grade:</strong> {profileData.class}</li>
                <li><strong>School:</strong> {profileData.school}</li>
                <li><strong>Location:</strong> {profileData.location}</li>
              </ul>
            </div>

            <div className="info-card">
              <h2>My Hobbies</h2>
              <ul className="hobbies-list">
                {profileData.hobbies.map((hobby, idx) => (
                  <li key={idx}>🎉 {hobby}</li>
                ))}
              </ul>
            </div>

            <div className="info-card">
              <h2>My Talent</h2>
              <p className="talent-text">
                <strong>✨ {profileData.talent}</strong>
              </p>
              <p>
                I love creating fictional worlds and stories. Writing helps me express my creativity 
                and imagination. I enjoy crafting engaging narratives that captivate readers.
              </p>
            </div>

            <div className="info-card">
              <h2>About Me</h2>
              <p>{profileData.about}</p>
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
