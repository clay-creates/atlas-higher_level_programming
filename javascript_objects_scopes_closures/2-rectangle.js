#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0) {
    }
    if (!Number.isInteger(h) || h <= 0) {
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
