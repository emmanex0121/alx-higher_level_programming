#!/usr/bin/node

const arg = process.argv[2];
const num = Number(arg);

if (arg === undefined) {
  console.log(1);
}

function factorial (num) {
  if (num < 0) {
    return undefined;
  }

  if (num === 0) {
    return 1;
  } else {
    return (num *= factorial(num - 1));
  }
}

if (!isNaN(num)) {
  console.log(factorial(num));
}
