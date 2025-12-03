nuberList=[]
let loop = true;

while (loop == true){
    const answer = prompt("Enter a number:");

    switch (answer) {
        case 'answer != 0':
            console.log(answer);
            numberList.push(answer);
            break;
        case 'answer = 0':
            loop = false;
            break;
        default:
            console.log("invalid answer");
            alert('Not a number.')
            break;

}
}
