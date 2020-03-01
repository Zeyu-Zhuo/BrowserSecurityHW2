function sendMessageToContentScript(message, callback)
{
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs)
    {
        chrome.tabs.sendMessage(tabs[0].id, message, function(response)
        {
            if(callback) callback(response);
        });
    });
}

// $(function(){
//     $('#input').keyup(function(){
//         $('#hello').text('hello ' + $('#input').val() + '!');
//     })
// })


$(function(){
    $("#replace").click(function(){
        var msg = $('#input').val();
        sendMessageToContentScript({cmd:'test', value: msg}, function(response){
            // console.log('response from content: '+response);
            });
    })
})



// $("#replace").click(function(){
//     var msg = $('#input').val();
//     sendMessageToContentScript({cmd:'test', value: '123'}, function(response){
//     // console.log('response from content: '+response);
//     });
// })

// sendMessageToContentScript({cmd:'test', value: '123'}, function(response)
// {
//     // console.log('response from content: '+response);
// });