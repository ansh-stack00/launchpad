const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const { pathname, query } = parsedUrl;

  if (pathname === '/echo') {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ headers: req.headers }, null, 2));
  }

  else if (pathname === '/slow') {
    const delay = parseInt(query.ms) || 1000;
    setTimeout(() => {
      res.end(`Responded after ${delay}ms`);
    }, delay);
  }

  else if (pathname === '/cache') {
    res.setHeader('Cache-Control', 'max-age=30');
    res.setHeader('ETag', '"12345"');
    if (req.headers['if-none-match'] === '"12345"') {
      res.statusCode = 304;
      res.end();
    } else {
      res.end('This response is cacheable');
    }
  }

  else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

server.listen(3000, () => console.log(" hurray 🥳🥳 server is listening on port 3000 "));
