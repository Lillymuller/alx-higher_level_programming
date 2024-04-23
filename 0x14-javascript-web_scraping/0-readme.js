#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8',
  function (error, body) {
    if (error) {
      console.log(error);
      return;
    } else {
    console.log(body);
    }
  });
