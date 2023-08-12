#!/usr/bin/node
const fs = require("fs");
const filePath = process.argv[2];
const writeData = process.argv[3];

fs.writefile(filePath, writeData, 'utf-8', (error) => {
	if (error) {console.log(error); }
});
