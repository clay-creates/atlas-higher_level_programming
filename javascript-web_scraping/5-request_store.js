#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiPath = process.argv[2];
const storagePath = process.argv[3];

request(apiPath, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(storagePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
