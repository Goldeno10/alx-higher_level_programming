#!/usr/bin/node
exports.esrever = function (list) {
  let lst = list.length - 1;
  let fst = 0;
  if (list.length > 1) {
    while ((fst !== lst) && fst < lst) {
      [list[lst], list[fst]] = [list[fst], list[lst]];
      fst++;
      lst--;
    }
  }
  return (list);
};
