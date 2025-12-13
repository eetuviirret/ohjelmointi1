/* Make an app that retrieves information about a TV series you enter and displays it in the console. (2p)
API to use: TVMaze API
First, make a valid HTML page with a search form. Example form:
<form action="https://api.tvmaze.com/search/shows">
  <input id="query" name="q" type="text">
  <input type="submit" value="Search">
</form>
Test the form. The result should be a page full of JSON formatted data.*/

/*Develop the app further.
Add JavaScript that gets the value entered to the
 form and sends a request with fetch to
  https://api.tvmaze.com/search/shows?q=${value_from_input}.
   Print the search result to the console.*/

/*Develop the app even further. Print the following information for all series from the search result on the web page. (7p)
required information: Name, link to details (url), medium image and summary
show the name in <h2> element
show the url in <a> element. Also add target="_blank" to the link.
show the medium image with <img src="" alt="">. Add medium image to src attribute and name property to alt attribute.
some TV-shows don't have images. This will cause an error. You can fix this by adding ? operator to image property. Example: tvShow.show.image?.medium;. This is called optional chaining.
show summary in <div> element (not <p>). This is because the summary is already in <p> element, and the result will not be valid if <p> is inside another <p>.
collect the elements to <article> elements and append <article> elements to the HTML document.
make <div id="results"> element to the HTML document where you append the <article> elements.
clear the old results with innerHTML = '' before you append the new results.*/

/*Develop the app even further. Optional chaining is not the best way to handle missing image.
Use ternary operator or if/else to add a default image if TV-show is missing image property. (2p)*/

'use strict';

let form = document.querySelector('form');
const query_input = document.getElementById('query');


async function tvInfo(event){
    event.preventDefault();
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query_input.value}`);
    const info = await response.json();


    //document.getElementById('answer').innerHTML = JSON.stringify(info[0]);
    console.log(query_input.value);
    console.log(info[0]);

    const name = info[0].show.name;
    console.log(name);
    const url = info[0].show.url;
    console.log(url);
    let image = info[0].show.image?.medium;
    //let image = "https://placehold.co/210x295?text=Not%20Found";
    console.log(image);

    if (image == null){
        image = "https://placehold.co/210x295?text=Not%20Found";
    }

    const summary = info[0].show.summary;
    console.log(summary);

    const print_answer = document.getElementById('print_answer');
    print_answer.innerHTML = '';

    const n = document.createElement('h2');
    n.textContent = name;
    print_answer.appendChild(n);

    const br = document.createElement("br");
    print_answer.appendChild(br);

    const u = document.createElement('a');
    u.href = url;
    u.textContent = url;
    u.target = '_blank';
    print_answer.appendChild(u);

    print_answer.appendChild(document.createElement("br"));

    const i = document.createElement('img');                // create img element
    i.src = image;
    i.alt = name;
    print_answer.appendChild(i);

    print_answer.appendChild(document.createElement("br"));

    const s = document.createElement('div');
    s.textContent = summary;
    print_answer.appendChild(s);

}
form.addEventListener('submit', tvInfo);




