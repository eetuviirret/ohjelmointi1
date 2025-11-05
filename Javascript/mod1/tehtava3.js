//Write a program that prompts for three integers.
// The program prints the sum, product and average of the numbers
// to the HTML document. (3p)
//remember to convert strings to numbers when adding them together.
'use strict';

const numbers = [];

 for (let i = 1; i<=3; i++)
{
    let number = parseInt(prompt('Enter an integer: '));
    numbers.push(number);
}

 let s = (numbers[0] + numbers[1] + numbers[2]);
 let p = (numbers[0] * numbers[1] * numbers[2]);
 let a = ((numbers[0] + numbers[1] + numbers[2])/numbers.length);

 document.querySelector('#sum').innerHTML = 'sum: ' + s;
 document.querySelector('#product').innerHTML = 'product: ' + p;
 document.querySelector('#average').innerHTML = 'average: ' + a;

//kesken