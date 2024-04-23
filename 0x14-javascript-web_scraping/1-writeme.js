#!/usr/bin/node

let fpath = process.argv[2];
let text = process.argv[3];
const fs = require('fs');
fs.writeFile(fpath, text, 'utf8', function (error) {
	if (error) {
		console.log(error);
	}
});
