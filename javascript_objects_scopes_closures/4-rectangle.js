#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || typeof (w) === 'undefined' || h < 1 || typeof (h) === 'undefined') {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    this.width = h;
    this.height = w;
  }

  double () {
    this.width = (w * 2);
    this.height = (h * 2);
  }
}

module.exports = Rectangle;
