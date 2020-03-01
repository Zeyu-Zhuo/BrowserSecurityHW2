function sendData(position) {
    console.log(position);
    $.ajax({
        type: "GET",
        url: "http://www.yourwebsite.com/",
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