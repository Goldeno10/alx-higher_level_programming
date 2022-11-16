#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (!err) {
    fs.writeFileSync(process.argv[3], body);
  }
});
