#!/usr/bin/node

exports.esrever = function (list) {
  let reverseList = [];
  for (let i = list.length; i >= 0; i--) {
    if (i === list.length - 1) {
      reverseList = [list[i]];
    } else {
      reverseList.push(list[i]);
    }
  }
  return (reverseList);
};
