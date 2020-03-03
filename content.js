var res = $("body").html().replace(/Chrome/ig,"Firefox")
$("body").html(res);

var imgURL = chrome.extension.getURL("new.png");
$('#logo').children('a').children('img').attr('src', imgURL);f