/*Write a program that prompts the user for numbers.
When the user enters one of the numbers previously entered,
the program will announce that the number has already been
given and stops its operation and then prints all the given
numbers to the console in ascending order. (2p)*/

numberList = [];

let number = Number(prompt('Enter a number:'));
while (!numberList.includes(number)) {
     numberList.push(number);
     number = Number(prompt("Enter a number:"));
 }

alert('Number is already on the list');
numberList.sort((a,b) => a-b);
console.log(numberList)

