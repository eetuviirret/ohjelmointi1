'use strict'

const confirmation = window.confirm('Should I calculate the square root?');
if (confirmation == true) {
let number = parseInt(prompt('Input number:'));
if (number < 0) {
document.querySelector('#result').innerHTML = 'The square root of negative number can not be defined.';
}
else {
let square = Math.sqrt(number);
document.querySelector('#result').innerHTML = String(square);
}}
else {
document.querySelector('#result').innerHTML = 'The square root is not calculated.';
}