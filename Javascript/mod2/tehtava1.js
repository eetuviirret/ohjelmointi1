const numbers = [];
for (let i = 1; i<= 5; i++) {
    numbers.push(prompt('Enter number: '));
}
console.log(numbers)
numbers.sort((a,b) => b-a);