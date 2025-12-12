const bullet = document.querySelector('#target');
const html =  `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>`;
bullet.innerHTML = html;

const second = bullet.getElementsByTagName('li')[1];
second.classList.add("my-list");