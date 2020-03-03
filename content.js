var imgURL = chrome.extension.getURL("new.png");

chrome.runtime.onMessage.addListener(function(request)
{
        if(request.cmd == 'test') {
        var regk = "/"+request.value[0]+'/ig'
        var reg = eval(regk)
        var res = $("body").html().replace(reg,request.value[1])
        $("body").html(res);
        $('#logo').children('a').children('img').attr('src', imgURL);
    }
});