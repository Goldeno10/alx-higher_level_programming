#!/usr/bin/node
'use strict';
const x = parseInt(process.argv[2]);
if (x) {
  let l = 1;
  while (x >= l) {
    console.log('X'.repeat(x));
    l++;
  }
} else {
  console.log('Missing size');
}
