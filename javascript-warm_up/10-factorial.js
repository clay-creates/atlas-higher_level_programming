#!/usr/bin/node

function Factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * Factorial(n - 1);
}

const arg = process.argv[2];
const num = parseInt(arg);

console.log(Factorial(num));
