#!/usr/bin/node

const arg = process.argv[2];
const num = Number(process.argv[2]);

if (arg === undefined) {
  console.log('Missing number of occurences');
}
/*
if (num < 0){
	console.log('');
}
*/
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
