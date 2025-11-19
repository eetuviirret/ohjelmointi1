'use strict'

const name = prompt('Enter your name: ');
let result = Math.ceil(Math.random()*4);
switch (result)
{
    case 1:
        console.log('You are... Gryffindor!');
        document.querySelector('#sorting').innerHTML = 'You are... Gryffindor!';
        break;
    case 2:
        console.log('You are... Slythering!');
        document.querySelector('#sorting').innerHTML = 'You are... Slythering!';
        break;
    case 3:
        console.log('You are... Rawenclaw!');
        document.querySelector('#sorting').innerHTML = 'You are... Rawenclaw!';
        break;
    case 4:
        console.log('You are... Hufflepuf!');
        document.querySelector('#sorting').innerHTML = 'You are... Hufflepuf!';
        break;
    default:
        console.log('You are... Muggle...');
        document.querySelector('#sorting').innerHTML = 'You are... Muggle...';
}
