#!/usr/bin/node

/*
Converter defines a function that returns another function,
the function that is returned takes a number as an argument
and then the results are returned via the toString method.
*/

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
