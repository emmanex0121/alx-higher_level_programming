#!/usr/bin/node

/*
exports.esrever = function (list) {
  return list.map((_, idx, arr) => arr[arr.length - 1 - idx]);
};
*/

//= =========== METHOD 2 ===========
exports.esrever = function (list) {
  const reverseList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return (reverseList);
};
