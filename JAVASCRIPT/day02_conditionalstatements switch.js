// 'use strict';

// process.stdin.resume();
// process.stdin.setEncoding('utf-8');

// let inputString = '';
// let currentLine = 0;

// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });

// process.stdin.on('end', _ => {
//     inputString = inputString.trim().split('\n').map(string => {
//         return string.trim();
//     });
    
//     main();    
// });

// function readLine() {
//     return inputString[currentLine++];
// }

function getLetter(s) {
    let letter;
    // Write your code here
    let alpha1 = s[0]
    // console.log(s[0])
    switch(true){
        case ['a','e','i','o','u'].includes(alpha1):
          letter = 'A';
          break;
        case ['b','c','d','f','g'].includes(alpha1):
          letter = 'B';
          break;
        case ['h','j','k','l','m'].includes(alpha1):
          letter = 'C';
          break;
        case ['n','p','q','r','s','t','v','w','x','y','z'].includes(alpha1):
          letter = 'D';
          break;

    }
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}