/*Write a program that asks the user for numbers until
 the user gives zero. The given numbers are printed
 in the console from the largest to the smallest. (2p)
 */

/*
Wanted to practice using switch.
This is unnessesary complicated and stupid way to do this.

numberList=[]
let loop = true;

while (loop === true) {
    const answer = Number(prompt("Enter a number:"));

    switch (true) {
        case isNaN(answer):
            console.log("invalid answer");
            alert("Not a number.");
            break;
        case answer === 0:
            loop = false;
            break;
        case answer !== 0:
            numberList.push(answer);
            break;
        default:
            console.log("invalid answer");
            alert('Not a number.')
            break;
    }
}
numberList.sort((a,b) => b-a);
console.log(numberList)
*/

numberList=[]
let answer = Number(prompt("Enter a number:"));

 while (answer !== 0) {
     numberList.push(answer);
     answer = Number(prompt("Enter a number:"));
 }
numberList.sort((a,b) => b-a);
console.log(numberList)