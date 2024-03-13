#!/usr/bin/node
const SQUARE = require('./5-square.js');

class Square extends SQUARE {
  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
