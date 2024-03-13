#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

Object.keys(dict).forEach((key, index) => {
  // dict[key] produces the value of the key at that index
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
});
console.log(newDict);

/*
const uniqueValues = Array.from(new Set(Object.values(dict)))

//const newDict = Object.assign(...Array.from(uniqueValues, (value) => ({[value]:[]})))

const newDict = Object.assign(...uniqueValues.map((value) => {
  return {[value]:[]}
  }

))

Object.keys(dict).forEach((key) => {
    newDict[dict[key]].push(key)
})
console.log(newDict);
*/
