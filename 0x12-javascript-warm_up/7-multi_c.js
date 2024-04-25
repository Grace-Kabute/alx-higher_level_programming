#!/usr/bin/node
const x = 'C is fun';
const number = parseInt(process.argv[2]);


if(process.argv.length <= 2 || isNaN(number)){
  console.log('Missing number of occurrences')
} else {
  for( let i = 0; i < number; i++){
	  console.log(x)
  }
}
