/*const targetList = document.querySelector('#target');

const bullet1 = document.createElement('li');
const bullet2 = document.createElement('li');
const bullet3 = document.createElement('li');

const text1 = document.createTextNode('First');
const text2 = document.createTextNode('Second');
const text3 = document.createTextNode('Third');

bullet1.appendChild(text1);
bullet2.appendChild(text2);
bullet3.appendChild(text3);

bullet2.classList.add("my-list");

targetList.appendChild(bullet1);
targetList.appendChild(bullet2);
targetList.appendChild(bullet3);

 */

const targetList = document.querySelector('#target');
const text = ['first','second','third'];

for  (let i=0; i<=2; i++) {
    const bullet = document.createElement('li')
    bullet.appendChild(document.createTextNode(text[i]));
    targetList.appendChild(bullet)

    if (i === 1){
        bullet.classList.add('my-list');
    }
}

