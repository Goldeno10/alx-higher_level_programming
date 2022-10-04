#!/usr/bin/node
'use strict';
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.height && this.width) {
      let len = 0;
      while (len < this.height) {
        console.log('X'.repeat(this.width));
        len++;
      }
    }
  }
};
