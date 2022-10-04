#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      if (this.height) {
        let len = 0;
        while (len < this.height) {
          console.log(c.repeat(this.width));
          len++;
        }
      }
    } else {
      this.print();
    }
  }
};
