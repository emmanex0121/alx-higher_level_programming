#!/usr/bin/node
const arr = require('./100-data').list;

const newArr = arr.map((element, index) => element * index);
console.log(arr);
console.log(newArr);
