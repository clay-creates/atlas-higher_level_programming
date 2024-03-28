#!/usr/bin/node

const request = require('request');

const apiPath = process.argv[2];

let count = 0;

request(apiPath, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        const tokens = character.split('/');
        if (tokens[5] === '18') {
          count++;
        }
      }
    }
  }
  console.log(count);
});
