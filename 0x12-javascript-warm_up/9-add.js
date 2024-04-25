#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (process.argv.length <= 3 || isNaN(size)) {
  console.log('NaN');
} else {
  for (let i = 0; i < size; i++) {
    console.log(process.argv[3] + process.argv[4]);
  }
}
