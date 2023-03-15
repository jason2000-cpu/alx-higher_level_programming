#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) {
  console.log('No arguments');
} else {
  console.log(`${argv[2]}`);
}
