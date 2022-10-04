#!/usr/bin/node
'use strict';
const args = process.argv.slice(2);
const arr = [];
if (args.length > 1) {
  args.forEach((value, index) => {
    arr.push(parseInt(value));
  });
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
} else {
  console.log(0);
}
