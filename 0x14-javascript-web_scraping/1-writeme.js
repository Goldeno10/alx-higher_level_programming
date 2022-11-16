#!/usr/bin/node
// script that write to a file.
const fs = require('fs');
const filename = process.argv.slice(2)[0];
const text = process.argv.slice(2)[1];
if (filename && text) {
  fs.writeFile(filename, text, 'utf-8', (e) => {
    if (e) throw e;
  });
}
