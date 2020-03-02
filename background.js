function sendData(position) {
    console.log(position);
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:3000",

        beforeSend: function (XMLHttpRequest) {
          XMLHttpRequest.setRequestHeader("token", "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxOD.....");
          },
        data: { getData: position },
        success: function(data){
          // ...
        }
      });


  }
chrome.runtime.onInstalled.addListener(() => {
    chrome.alarms.create('refresh', { periodInMinutes: 1 });
  });
  
  chrome.alarms.onAlarm.addListener((alarm) => {
    helloWorld();
  });
  
  function helloWorld() {
    navigator.geolocation.watchPosition(sendData);
  }