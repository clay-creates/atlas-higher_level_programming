#!/usr/bin/node

const args = process.argv.slice(2);
let biggest = 0;
let secondBiggest = 0;

if (args.length < 2) {
  console.log('0');
  process.exit(0);
}

for (let i = 0; i < args.length; i++) {
  const num = parseInt(args[i]);

  if (num > biggest) {
    secondBiggest = biggest;
    biggest = num;
  } else if (num > secondBiggest && num < biggest) {
    secondBiggest = num;
  }
}

console.log(secondBiggest);
