#!/usr/bin/node
'use strict';
let arr = parseInt(process.argv[2]);
if (arr) {
  while (arr > 0) {
    console.log('C is fun');
    arr--;
  }
} else {
  console.log('Missing number of occurrences');
}
