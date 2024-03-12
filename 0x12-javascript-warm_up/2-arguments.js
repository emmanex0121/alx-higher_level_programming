#!/usr/bin/node
const argLength = process.argv.length;
if (argLength === 3) {
  console.log('Argument found');
} else if (argLength > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
// OR in a single line using ternary operators
// console.log(count === 2 ? 'No argument' : count === 3 ?
// 'Argument found' : 'Arguments found');
