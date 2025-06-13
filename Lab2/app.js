const express = require('express');
const app = express();
const path = require('path');

// Serve static files from 'public' folder
app.use(express.static('public'));

// Serve main page at root route '/'
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/Lab2.html'));
});

// Route 1: Path parameter
app.get('/about/:name', (req, res) => {
  res.send(`You're viewing the about page for ${req.params.name}.`);
});

// Route 2: Query string
app.get('/greet', (req, res) => {
  const name = req.query.name || 'visitor';
  res.send(`Hello, ${name}! Welcome to Audrey's site.`);
});

// Route 3: Path + query
app.get('/mood/:cat', (req, res) => {
  const { cat } = req.params;
  const { mood } = req.query;
  res.send(`${cat} is feeling ${mood || 'happy'}.`);
});

// Route 4: Another path parameter
app.get('/favorites/:thing', (req, res) => {
  res.send(`Audrey's favorite ${req.params.thing} is turkey.`);
});

// Route 5: Schedule query param
app.get('/schedule', (req, res) => {
  const time = req.query.time;
  if (time === 'morning') {
    res.send('Audrey naps in the sun.');
  } else if (time === 'night') {
    res.send('Audrey hunts for mice.');
  } else {
    res.send('Audrey is probably napping.');
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
