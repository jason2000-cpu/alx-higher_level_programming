#!/usr/bin/node
const { argv } = require('node:process');


if (argv[2]) {
  console.log(typeof(parseInt(argv[2])))
} else {
  console.log('Not a number')
}