const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get('/api/about', (req, res) => {
  res.json({
    name: 'Ayush Pandey',
    class: '10th',
    school: 'Silver Grove School',
    location: 'Varanasi, Uttar Pradesh',
    hobbies: ['Dance', 'Singing'],
    talent: 'Writing Stories'
  });
});

app.get('/api/stories', (req, res) => {
  res.json([
    {
      id: 1,
      title: 'The Mystery of the Old Library',
      excerpt: 'A tale of hidden secrets and forgotten mysteries...',
      date: '2025-01-15'
    },
    {
      id: 2,
      title: 'Journey Through the Desert',
      excerpt: 'An adventure story of courage and survival...',
      date: '2025-02-10'
    },
    {
      id: 3,
      title: 'The Last Kingdom',
      excerpt: 'A fantasy story of magic and kingdoms...',
      date: '2025-03-05'
    }
  ]);
});

app.get('/api/skills', (req, res) => {
  res.json({
    talents: ['Storytelling', 'Creative Writing', 'Imagination'],
    hobbies: ['Dancing', 'Singing', 'Reading'],
    learning: ['Web Development', 'JavaScript', 'React']
  });
});

app.post('/api/contact', (req, res) => {
  const { name, email, message } = req.body;
  
  // Here you would typically save this to a database
  console.log('Contact message:', { name, email, message });
  
  res.json({
    success: true,
    message: 'Thank you for reaching out! I will get back to you soon.'
  });
});

app.get('/', (req, res) => {
  res.json({ message: 'Welcome to Ayush Pandey\'s Portfolio API' });
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
