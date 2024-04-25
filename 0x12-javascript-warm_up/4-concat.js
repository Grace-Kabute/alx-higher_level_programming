#!/usr/bin/node
if (process.argv.length <= 2 || process.argv.slice(2).every(arg => arg === '')){
    console.log('undefined');
} else {
    console.log(process.argv.slice(2).join(' is '));
}
