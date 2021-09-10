$(document).ready(function() {
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
});

$('#comment-delete-btn').click(function () {
    $("#comment-delete-modal").addClass("is-active");
});

$('#comment-delete-close').click(function () {
    $('#comment-delete-modal').removeClass('is-active');
});

