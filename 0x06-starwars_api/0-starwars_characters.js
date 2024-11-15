#!/usr/bin/node
const util = require('util');
const request = require('request');

const promisifiedRequest = util.promisify(request);

async function getFilmWithId (filmId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;
  try {
    const response = await promisifiedRequest(url);
    if (response.statusCode !== 200) {
      throw new Error(`${response.statusCode}: Something Went Wrong`);
    }
    return JSON.parse(response.body);
  } catch (err) {
    throw new Error(`Failed to get the film: ${err.message}`);
  }
}

async function getCharactersOfFilm (filmObj) {
  const characters = [];
  const people = filmObj.characters;

  for (const person of people) {
    try {
      const response = await promisifiedRequest(person);
      if (response.statusCode !== 200) {
        throw new Error(`${response.statusCode}: Something Went Wrong while fetching people`);
      }
      characters.push(JSON.parse(response.body).name);
    } catch (err) {
      throw new Error(`Failed to get characters: ${err.message}`);
    }
  }
  return characters;
}

async function main () {
  try {
    const filmId = process.argv[2];
    const filmObj = await getFilmWithId(filmId);
    const charactersArray = await getCharactersOfFilm(filmObj);
    charactersArray.forEach(name => console.log(name));
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

main();
