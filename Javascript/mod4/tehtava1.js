'use strict';

let form = document.querySelector('form');
const query = document.getElementById('query');


async function tvInfo(event){
    event.preventDefault();
    const responce = await fetch(`https://api.tvmaze.com/search/shows?q=${query.value}`);
    const info = await responce.json();

   /* console.log(info[0]);
    console.log(info[0].show);
    const name = info[0].show.name;
    const message = info[0].show.message;
    const code = info[0].show.code;
    const status = info[0].show.status;*/

    document.getElementById('answer').innerText = info;

}
form.addEventListener('submit', tvInfo);
