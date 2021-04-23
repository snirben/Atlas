
$( document ).ready(function() {

var steps=0;

const cards = document.querySelectorAll('.memory-card');




(function shuffle() {
  cards.forEach(card => {
    let randomPos = Math.floor(Math.random() * 12);
    card.style.order = randomPos;
  }); });
});

