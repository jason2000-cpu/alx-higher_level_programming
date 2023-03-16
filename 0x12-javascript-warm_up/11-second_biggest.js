#!/usr/bin/node

let arr = process.argv.slice(2);
let newArr = [];

if (arr.length  <= 1) {
    console.log(0)
} else {
   console.log(arr.splice(arr.indexOf(Math.max(arr)), 1));
    for (let i = 0; i < arr.length; i++){
        for (let j = 0; i < 1; j++){
            console.log(i, ':', j);
        }
    }
   //console.log(newArr[0])
}

