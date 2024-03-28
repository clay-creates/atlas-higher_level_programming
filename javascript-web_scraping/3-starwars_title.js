#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiPath = 'https://swapi-api.hbtn.io/api/films/:id';

request(apiPath, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.id === movieID) {
    console.log(response.title);
  }
});
