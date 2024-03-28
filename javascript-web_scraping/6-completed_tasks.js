#!/usr/bin/node

const request = require('request');

const apiPath = process.argv[2];

exports.tasksCompleted = function () {
  request(apiPath, { json: true }, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const completedTasks = body.filter(task => task.completed);
    const completedTasksByUser = {};

    completedTasks.forEach(task => {
      const userId = task.userId;
      completedTasksByUser[userId]++;
    });
    for (const userId in completedTasksByUser) {
      console.log(`'${userId}': ${completedTasksByUser[userId]}`);
    }
  });
};

exports.tasksCompleted();
