$( document ).ready(function() {

var steps = 0;
var random = Math.floor(Math.random()*9);
var items = $('.pic-group');
var index = 0;
const buttons = document.querySelectorAll('.btn');
init();

function getrandom(){
    random = Math.floor(Math.random()*9);
}

function cloneitem(item){
    for(let i = 0; i < random; i++){
    item.clone().insertAfter(item);
    }
}

function init(){
    cloneitem(items.eq(index).children());
}
function incsteps(){
    steps+=1;
    $('#steps').text(steps);
}

function checkmatch(){
    incsteps();
    if(random === $(this).attr('id')-1){

        if(checkend()){
            endgame();
            return;
        }
        getrandom();
        items[index].style.display = 'none';
        index += 1;
        cloneitem(items.eq(index).children());
        items[index].style.display = 'block';
    }
    else{

    }
}

function checkend(){
    console.log(items.length);
        console.log(index);

    if(items.length === index+1){
    return true;
    }
    return false;
}
function endgame(){
    $.ajax({
            url: "/ajax/save-someinthepicture-result/",
            data: {
                'steps': steps,
                'game_id': $("section")[0].id
            },
            success: function () {

            }
        });
}

buttons.forEach(btn => btn.addEventListener('click', checkmatch));





});