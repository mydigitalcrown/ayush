import React from 'react';
import './Footer.css';

function Footer() {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container footer-container">
        <p>&copy; {currentYear} Ayush Pandey. All rights reserved.</p>
        <div className="social-links">
          <a href="#" title="Twitter">𝕿</a>
          <a href="#" title="Facebook">f</a>
          <a href="#" title="Instagram">📷</a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
