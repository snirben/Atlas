
$( document ).ready(function() {

const cards = document.querySelectorAll('.memory-card');
var steps = 0;
var matchcards = 0;
let hasFlippedCard = false;
let lockBoard = false;
let firstCard, secondCard;

function incsteps(){
  steps+=1;
}

function flipCard() {
  var num = $(this).attr('id');
  var name = 'audio-'+ num;
  var audioElem = $('#'+name);
  audioElem[0].play();

    incsteps();
    return;
  }



function checkForMatch() {
  let isMatch = firstCard.dataset.framework === secondCard.dataset.framework;

  isMatch ? disableCards() : unflipCards();
}

function disableCards() {
  firstCard.removeEventListener('click', flipCard);
  secondCard.removeEventListener('click', flipCard);
  matchcards+=1;
  resetBoard();

  if(Checkend()){
    endgame();
  }

}

function showsteps(){
  $("#steps").text(steps);
}
function unflipCards() {
  lockBoard = true;

  setTimeout(() => {
    firstCard.classList.remove('flip');
    secondCard.classList.remove('flip');

    resetBoard();
  }, 1500);
}

function resetBoard() {
  [hasFlippedCard, lockBoard] = [false, false];
  [firstCard, secondCard] = [null, null];
}

function Checkend(){
  if (cards.length/2 === matchcards){
    return true;
  }
  return false;
}
function endgame(){

$.ajax({
            url: "/ajax/save-game-result/",
            data: {
                'steps': steps,
                'game_id': $("section")[0].id
            },
            success: function () {

            }
        });
}

(function shuffle() {
  cards.forEach(card => {
    let randomPos = Math.floor(Math.random() * 12);
    card.style.order = randomPos;
  });
})();


cards.forEach(card => card.addEventListener('click', flipCard));
});
