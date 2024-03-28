#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiPathRequest = 'https://swapi-api.hbtn.io/api/films/:id' + movieID;

request(apiPathRequest, function (error, response, body) {
    if (error) {
        console.error(error);
    } else {
        const data = JSON.parse(body);
        console.log(data.title);
    }
});
