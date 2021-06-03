

$( document ).ready(function() {
var index = 0;
var steps=0
var match = 0;
const colors= document.querySelectorAll('.btn');
const array = document.querySelectorAll('#main_img')
const size = array.length
function checkcolor(){

var audio = "audio-" + $(this).attr('id');
$('#' + audio)[0].play();

incstep()

if($(this).attr('id') === $(this).parent().attr('id')){
    var x = $(this).parent().parent()
    console.log($(this))
    console.log(x)
    x[0].style.display = "none";
    match+=1;
    if (match === size){
        array[index].style.display = "none";
        $('#hide')[0].style.display = 'none';
        endgame();
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

function endgame(){
    console.log($('.container')[1]);
    $.ajax({
            url: "/ajax/save-colorgame-result/",
            data: {
                'steps': steps,
                'game_id': $("section")[0].id
            },
            success: function () {
              setTimeout(() => {
                $('#hide')[0].style.display = 'none';
                $('#done')[0].style.display = 'block';
              }, 1500);
            }
        });
}


colors.forEach(color=>color.addEventListener('click',checkcolor));


});

