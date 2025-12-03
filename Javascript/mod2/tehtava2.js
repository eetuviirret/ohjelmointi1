let numberOfParticipants = parseInt(prompt('Enter number of paricipants: '));
console.log(numberOfParticipants);
let participants = [];
for (let i = 1; i<= numberOfParticipants; i++) {
    participants.push(prompt('Enter a participant: '));
}
participants.sort();
for (let i = 0; i<= numberOfParticipants; i++) {
    const li = document.createElement("li");
    li.textContent = participants[i];
    document.getElementById("participants_list").appendChild(li)
}