#!/usr/bin/node
const argLength = process.argv.length;
if (argLength === 3) {
  console.log('Argument found');
} else if (argLength > 2) {
  console.log('Arguments found');
} else {
  console.log('NO arguments');
}
