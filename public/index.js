const express = require('express');
const request = require('request');

const app = express();

app.use('/maps/api', (req, res) => {
  const url = `https://maps.googleapis.com${req.url}&key=${process.env.API_KEY}`;
  req.pipe(request(url)).pipe(res);
});

app.listen(3000);
