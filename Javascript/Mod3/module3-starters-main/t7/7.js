const trigger = document.getElementById('trigger');

function A(evt){
document.getElementById('target').src = 'img/picB.jpg';                 // the attribute name is used as the property
document.getElementById('target').setAttribute('src', 'img/picB.jpg');
}
trigger.addEventListener('mouseover', A);

function B(evt){
document.getElementById('target').src = 'img/picA.jpg';                 // the attribute name is used as the property
document.getElementById('target').setAttribute('src', 'img/picA.jpg');
}
trigger.addEventListener('mouseout', B);