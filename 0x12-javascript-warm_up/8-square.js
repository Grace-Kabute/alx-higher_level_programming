#!/usr/bin/node
const x = 'x';
const size = parseInt(process.argv[2]);

if (process.argv.length <= 2 || isNaN(size)) {
  console.log('Missing size of the square');
} else {
  for (let i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
}
