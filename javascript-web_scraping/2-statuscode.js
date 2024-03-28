#!/usr/bin/node

const request = require('request');

const getURL = process.argv[2];

request(getURL, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
