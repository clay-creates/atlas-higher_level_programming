#!/usr/bin/node

const size = process.argv[2];

const sizeInt = parseInt(size, 10);

if (isNaN(sizeInt)) {
  console.log('Missing size');
} else {
  const x = 0;
  while (x < size) {
    for (let y = 0; y < sizeInt; y++) {
      console.log('X');
    }
    console.log('\n');
  }
}
