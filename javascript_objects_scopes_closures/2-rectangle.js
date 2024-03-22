#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || typeof (w) === 'undefined') {
    }
    if (h < 1 || typeof (h) === 'undefined') {
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
