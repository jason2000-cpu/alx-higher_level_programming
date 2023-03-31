#!/usr/bin/node
const number = process.argv[2];
if (!number || Number.isNaN(parseInt(number))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(number); i++) {
    console.log('C is fun');
  }
}
