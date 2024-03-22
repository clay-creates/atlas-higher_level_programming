#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  a = arg1;
  b = arg2;
  console.log(`${a + b}`);
}
