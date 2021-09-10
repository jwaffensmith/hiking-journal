$(document).ready(function() {
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
});

$('#delete-btn').click(function () {
    $("#delete-modal").addClass("is-active");
});

$('#delete-cancel').click(function () {
    $('#delete-modal').removeClass('is-active');
});

// $('#delete-btn').on('click', function (e) {
//     $("#delete-modal").addClass("is-active");
// });

// $('#delete-cancel').on('click', function (e) {
//     $('#delete-modal').removeClass('is-active');
// });