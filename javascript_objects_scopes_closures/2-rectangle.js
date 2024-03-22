#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (!Number.isInteger(w) || w <= 0) {
            return Rectangle{ };
        }
        if (!Number.isInteger(h) || h <= 0) {
            return Rectangle{ };
        }
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;
