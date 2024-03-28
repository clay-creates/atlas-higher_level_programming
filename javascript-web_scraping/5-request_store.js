#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiPath = process.argv[2];
const storagePath = process.argv[3];

request(apiPath, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    return data;
  }
});

fs.writeFile(storagePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Webpage data written to ${storagePath}`);
  }
});
