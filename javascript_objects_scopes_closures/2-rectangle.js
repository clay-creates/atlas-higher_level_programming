#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || typeof (w) === 'undefined' || h < 1 || typeof (h) === 'undefined') {
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
