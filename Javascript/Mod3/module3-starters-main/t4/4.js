'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const targetList = document.getElementById('target');

for  (let i=0; i<students.length; i++) {
    const bullet = document.createElement('option')
    bullet.value = students[i].id;
    bullet.textContent = students[i].name;
    targetList.appendChild(bullet);
}


