#!/usr/bin/node

const size = process.argv[2];

const sizeInt = parseInt(size, 10);

if (isNaN(sizeInt)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < sizeInt; y++) {
    let line = '';
    for (let y = 0; y < sizeInt; y++) {
      line += 'X';
    }
    console.log(line);
  }
}
