#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (!err) {
    fs.writeFileSync(process.argv[3], body);
  }
});
