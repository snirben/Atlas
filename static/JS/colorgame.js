

$( document ).ready(function() {
var index = 0;
var steps=0
var match = 0;
const colors= document.querySelectorAll('.btn');
const array = document.querySelectorAll('#main_img')
const size = array.length
console.log(size)
function checkcolor(){

var audio = "audio-" + $(this).attr('id');
$('#' + audio)[0].play();

incstep()

if($(this).attr('id') === $(this).parent().attr('id')){
    var x = document.getElementById("main_img");
    x.style.display = "none";
    match+=1;
    if (match === size){
        array[index].style.display = "none";
        return;
    }
    index+=1;
    array[index].style.display = "block";


}
}

function incstep(){

steps+=1;
$('#steps').text(steps)
}

colors.forEach(color=>color.addEventListener('click',checkcolor));


});

