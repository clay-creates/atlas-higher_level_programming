#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add = function add (a, b) {
  const sum = Number(a) + Number(b);
  console.log(`${sum}`);
};

require('13-add.js');
add(arg1, arg2);
