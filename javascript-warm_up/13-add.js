#!/usr/bin/node

function add (a, b) {
  const sum = Number(a) + Number(b);
  console.log(`${sum}`);
}

exports.add = add;
