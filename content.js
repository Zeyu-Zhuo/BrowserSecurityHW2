// reference: https://stackoverflow.com/questions/5558613/replace-words-in-the-body-text/50537862
var all = document.getElementsByTagName("*");
var res = $("body").html().replace(/Chrome/ig,"Firefox")
$("body").html(res);

// reference: https://blog.lateral.io/2016/04/create-chrome-extension-modify-websites-html-css/
var imgURL = chrome.extension.getURL("new.png");
$('#logo').children('a').children('img').attr('src', imgURL);

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse)
{
    // console.log(sender.tab ?"from a content script:" + sender.tab.url :"from the extension");
    if(request.cmd == 'test') alert(request.value);
});