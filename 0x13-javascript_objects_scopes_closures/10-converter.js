#!/usr/bin/node
exports.converter = function (base) {
  function converte (number) {
    return (number.toString(base));
  }
  return converte;
};
