#!/usr/bin/node

const args = process.argv.slice();

if (args.length === 0) {
  console.log('No argument');
} else {
  console.log(args[1]);
}
