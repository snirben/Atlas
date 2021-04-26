
$( document ).ready(function() {

var steps=0;
let firstCard, secondCard;

const cards = document.querySelectorAll('.memory-card');

function flipCard() {
  var num = $(this).attr('id');
  var name = 'audio-'+ num;
  var audioElem = $('#'+name);
  audioElem[0].play();


    return;
  }

function resetBoard() {
  [hasFlippedCard, lockBoard] = [false, false];
  [firstCard, secondCard] = [null, null];
}

(function shuffle() {
  cards.forEach(card => {
    let randomPos = Math.floor(Math.random() * 12);
    card.style.order = randomPos;
  }); });
});

