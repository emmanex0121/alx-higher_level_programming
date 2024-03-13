#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let arr;
      if (arr === undefined) {
        arr = 'X';

        for (let j = 0; j < this.width - 1; j++) {
          arr += 'X';
        }
      }
      console.log(arr);
    }
  }
}

module.exports = Rectangle;
