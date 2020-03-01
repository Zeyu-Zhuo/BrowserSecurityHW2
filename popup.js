$(function(){
    $('#input').keyup(function(){
        $('#hello').text('hello ' + $('#input').val() + '!');
    })
})