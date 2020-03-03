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

$(function(){
    $("#replace").click(function(){
        var replaceinput = $('#replaceinput').val();
        var withinput = $('#withinput').val();
        sendMessageToContentScript({cmd:'test', value: [replaceinput,withinput]}, function(response){
            });
    })
})