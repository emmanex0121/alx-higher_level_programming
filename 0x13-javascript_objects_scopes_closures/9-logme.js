#!/usr/bin/node

let arr = [];

exports.logMe = function (item) {
  if (arr[0] === undefined) {
    arr = [item];
  } else {
    arr.push(item);
  }
  const lenArr = arr.length - 1;
  console.log(lenArr + ': ' + item);
};
