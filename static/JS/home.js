$(document).ready( function () {
    $('#report').DataTable();
    $(document).on('click', '.select_star', function () {

      $.ajax({
            url: "ajax/create-star/",
            data: {
                'user_id': $(this).attr("data-frame"),
            },
            success: function () {
            location.reload();
            }
        });

    });
} );

