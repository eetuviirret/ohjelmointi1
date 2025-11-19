'use strict'

let year = prompt('Enter year: ')

if ((year % 4 == 0)||((year % 400 == 0)&&(year%100==0)))
{
    console.log('leap year')
    document.querySelector('#notification').innerHTML = 'leap year';
}
else
{
    console.log('not leap year')
    document.querySelector('#notification').innerHTML = 'not leap year';
}