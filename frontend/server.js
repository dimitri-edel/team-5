import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// MIME type mapping
const mimeTypes = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.mjs': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.wav': 'audio/wav',
  '.mp4': 'video/mp4',
  '.woff': 'application/font-woff',
  '.ttf': 'application/font-ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.otf': 'application/font-otf',
  '.wasm': 'application/wasm'
};

// Serve static files from the dist directory
app.use(express.static(path.join(__dirname, 'dist'), {
  index: false, // Don't serve index.html for /
  setHeaders: (res, filePath) => {
    const ext = path.extname(filePath).toLowerCase();
    const contentType = mimeTypes[ext] || 'application/octet-stream';
    res.setHeader('Content-Type', contentType);
    
    // Set appropriate cache headers
    if (filePath.endsWith('.html')) {
      res.setHeader('Cache-Control', 'no-cache');
    } else {
      res.setHeader('Cache-Control', 'public, max-age=31536000');
    }
  }
}));

// Proxy API requests to the backend
app.use('/api', (req, res) => {
  const apiUrl = process.env.NODE_ENV === 'production' 
    ? 'https://team5-api-eu-5d24fa110c36.herokuapp.com'  // Remove /api since it's already in the path
    : 'http://127.0.0.1:8000';
  
  // Forward the request to the API
  fetch(`${apiUrl}${req.url}`, {
    method: req.method,
    headers: {
      ...req.headers,
      host: new URL(apiUrl).host
    },
    body: req.method !== 'GET' ? JSON.stringify(req.body) : undefined
  })
  .then(apiRes => apiRes.json())
  .then(data => res.json(data))
  .catch(error => {
    console.error('API proxy error:', error);
    res.status(500).json({ error: 'Failed to fetch from API' });
  });
});

// Serve index.html for all other routes (SPA support)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Server error:', err.stack);
  res.status(500).send('Something went wrong!');
});

// Start server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend server is running on port ${PORT}`);
  console.log(`Serving static files from: ${path.join(__dirname, 'dist')}`);
}).on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Port ${PORT} is already in use`);
    process.exit(1);
  } else {
    console.error('Server error:', err);
    process.exit(1);
  }
}); 