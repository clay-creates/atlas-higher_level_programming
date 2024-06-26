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
      if (!completedTasksByUser[userId]) {
        completedTasksByUser[userId] = 0;
      }
      completedTasksByUser[userId]++;
    });
    let formattedOutput = JSON.stringify(completedTasksByUser, null, 2);
    formattedOutput = formattedOutput.replace(/"/g, "'");
    console.log(formattedOutput);
  });
};

exports.tasksCompleted();
