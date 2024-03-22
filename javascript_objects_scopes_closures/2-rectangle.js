#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0) {
      typeof (w) === 'undefined';
    }
    if (!Number.isInteger(h) || h <= 0) {
      typeof (h) === 'undefined';
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
