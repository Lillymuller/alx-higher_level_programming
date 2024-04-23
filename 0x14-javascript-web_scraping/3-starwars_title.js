#!/usr/bin/node

let id = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
