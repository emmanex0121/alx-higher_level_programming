#!/usr/bin/node

const arg = process.argv[2];
const num1 = Number(arg);
const num2 = Number(process.argv[3]);
//const argLen = process.argv.length;

/*
if (arg === undefined || isNaN(num1) || isNaN(num2) || argLen === 3){
	console.log('NaN');
}else{
	const sum = num1 + num2;
	console.log(sum);
}
*/
const sum = num1 + num2;
console.log(sum);

