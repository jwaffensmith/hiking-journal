$(document).ready(function() {
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
});

$('#delete-btn').on('click', function (e) {
    $("#delete-modal").addClass("is-active");
});

$('#delete-cancel').on('click', function (e) {
    $('#delete-modal').removeClass('is-active');
});

$('#delete-cancel-btn').on('click', function (e) {
    $('#delete-modal').removeClass('is-active');
});

$('#delete-comment-btn').on('click', function (e) {
    $("#delete-comment-modal").addClass("is-active");
});

$('#delete-comment-cancel').on('click', function (e) {
    $('#delete-comment-modal').removeClass('is-active');
});

$('#delete-comment-cancel-btn').on('click', function (e) {
    $('#delete-comment-modal').removeClass('is-active');
});

$('#comment-edit-btn').click(function () {
    $("#comment-edit-modal").addClass("is-active");
});

$('#comment-edit-close').click(function () {
    $('#comment-edit-modal').removeClass('is-active');
});

$('#edit-comment-cancel-btn').click(function () {
    $('#comment-edit-modal').removeClass('is-active');
});

$('#hike-edit-btn').click(function () {
    $("#hike-edit-modal").addClass("is-active");
});

$('#hike-edit-close').click(function () {
    $('#hike-edit-modal').removeClass('is-active');
});

$('#hike-edit-cancel-btn').click(function () {
    $('#hike-edit-modal').removeClass('is-active');
});