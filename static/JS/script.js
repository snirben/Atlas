$(document).click(function(event) {
    var num = $(event.target).parent().attr('id');
    var name = 'audio-'+ num;
    var audioElem = $('#'+name);
    audioElem[0].play();
});

$(document).ready( function () {
    $('#gananotdata').DataTable();
} );