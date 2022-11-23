#!/usr/bin/node
// script that prints the title of a Star Wars movie
//  where the episode number matches a given integer
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
if (id) {
  request(url, (e, res, body) => {
    if (!e) {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}
