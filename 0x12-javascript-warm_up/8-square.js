#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (arg === undefined || isNaN(num)) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let arr;
  if (arr === undefined) {
    arr = 'X';
    for (let j = 0; j < num - 1; j++) {
      arr += 'X';
    }
  }
  console.log(arr);
}
