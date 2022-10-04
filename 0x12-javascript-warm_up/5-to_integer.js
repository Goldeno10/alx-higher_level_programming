#!/usr/bin/node
'use strict';
const arg1 = parseInt(process.argv[2]);
if (arg1) {
  console.log(`My number: ${arg1}`);
} else {
  console.log('Not a number');
}
