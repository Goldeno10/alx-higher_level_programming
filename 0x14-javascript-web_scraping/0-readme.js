#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');
const filename = process.argv.slice(2)[0];

if (filename) {
  fs.readFile(filename, 'utf8', (e, data) => {
    if (e) throw e;
    console.log(data.toString());
  });
}
