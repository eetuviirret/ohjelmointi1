let numberOfParticipants = parseInt(prompt('Enter number of paricipants: '));
console.log(numberOfParticipants);
let participants = [];
for (let i = 1; i<= numberOfParticipants; i++) {
    participants.push(prompt('Enter a participant: '));
}
console.log(participants);