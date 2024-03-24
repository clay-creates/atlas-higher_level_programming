#!/usr/bin/node

/*
logMe begins with an IIFE (Immediately Invoked Function Expression),
that creates an internal variable: count. This variable can be reached
by the nested function created that prints the function call count
and the item passed to the nested function, then increments the count.

Creating this internal variable using IIFE allows for persisting memory
of the state of the count variable, while also making the count variable
inaccessable from outside of the IIFE.
*/

exports.logMe = (function () {
  let count = 0;
  return function (item) {
    console.log(`${count}: ${item}`);
    count++;
  };
})();
