#!/usr/bin/node
exports.esrever = function (list) {
  const list2 = [];
  for (let l = (list.length - 1); l >= 0; l--) {
    list2.push(list[l]);
  }
  return list2;
};
