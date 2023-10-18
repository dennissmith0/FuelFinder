require('dotenv').config();

// Now process.env.API_KEY is available
// console.log(process.env.API_KEY);

const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('.'));  // Serve static files from the current directory

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
