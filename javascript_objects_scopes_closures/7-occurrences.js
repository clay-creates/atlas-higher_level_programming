#!/usr/bin/node

exports.nbOccurences = funtion(list, searchElement) {
    return list.filter(element => element === searchElement).length;
};