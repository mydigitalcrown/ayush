# Ayush Pandey's Personal Portfolio Website

A full-stack personal portfolio website built with **React** (frontend) and **Node.js/Express** (backend).

## 📋 Features

- **Home Page**: Hero section with introduction and highlights
- **About Page**: Personal information, hobbies, and talents
- **Stories Page**: Display of creative stories with data from API
- **Contact Page**: Contact form to get in touch
- **Responsive Design**: Mobile-friendly layout
- **Modern UI**: Gradient backgrounds and smooth animations

## 🛠️ Tech Stack

**Frontend:**
- React 18
- React Router v6
- Axios for API calls
- CSS3 with modern styling

**Backend:**
- Node.js
- Express.js
- CORS enabled
- RESTful API

## 📁 Project Structure

```
ayush/
├── backend/
│   ├── server.js          # Main server file
│   ├── package.json       # Backend dependencies
│   ├── .env              # Environment variables
│   └── routes/           # API routes (expandable)
├── frontend/
│   ├── public/           # Static files
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   ├── pages/        # Page components
│   │   ├── App.js        # Main App component
│   │   └── index.js      # React entry point
│   └── package.json      # Frontend dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Setup Instructions

#### 1. Install Backend Dependencies
```bash
cd backend
npm install
```

#### 2. Install Frontend Dependencies
```bash
cd ../frontend
npm install
```

#### 3. Start the Backend Server
```bash
cd backend
npm run dev
# or for production
npm start
```
Server will run on `http://localhost:5000`

#### 4. Start the Frontend (in a new terminal)
```bash
cd frontend
npm start
```
App will open at `http://localhost:3000`

## 📝 API Endpoints

- `GET /` - Welcome message
- `GET /api/about` - Get profile information
- `GET /api/stories` - Get all stories
- `GET /api/skills` - Get skills and learning data
- `POST /api/contact` - Submit contact form

## 📖 Pages

### Home
- Hero section with introduction
- Three highlight cards (Storytelling, Dancing, Singing)
- Navigation to other pages

### About
- Personal information
- Hobbies and interests
- Talent showcase

### Stories
- Grid of story cards
- Story titles, excerpts, and dates
- "Read More" buttons

### Contact
- Contact information display
- Contact form with validation
- Success message on submission

## 🎨 Customization

### To modify your personal information:
Edit `backend/server.js` in the `/api/about` endpoint

### To add new stories:
Update the stories array in `/api/stories` endpoint

### To change styling:
Modify CSS files in `frontend/src/` directory

## 📱 Responsive Design
The website is fully responsive and works on:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (below 768px)

## 🚀 Deployment

### Deploy Backend:
- Heroku, Railway, Vercel, or similar platforms

### Deploy Frontend:
- Vercel, Netlify, or GitHub Pages

## 📧 Contact
- Location: Varanasi, Uttar Pradesh
- School: Silver Grove School
- Grade: 10th

## 📄 License
This project is personal and free to use.

---

**Created by:** Ayush Pandey  
**Last Updated:** March 2026
