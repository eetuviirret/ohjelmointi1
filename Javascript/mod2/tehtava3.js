let dogList = [];
for (let i = 1; i<= 6; i++) {
    dogList.push(prompt('Enter a dog: '));}
console.log(dogList)

dogList.sort().reverse();
for (let i = 0; i<= 5; i++) {
    const li = document.createElement("li");
    li.textContent = dogList[i];
    document.getElementById("ulDogList").appendChild(li)
}