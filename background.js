// console.log('hello background')
function scrollMap(position) {
    // Scrolls the map so that it is centered at
    //  (position.coords.latitude, position.coords.longitude).
    console.log(position);
  }
  
  // Request repeated updates.
  //var watchId = navigator.geolocation.watchPosition(scrollMap);

//reference: https://levelup.gitconnected.com/how-to-use-background-script-to-fetch-data-in-chrome-extension-ef9d7f69625d
chrome.runtime.onInstalled.addListener(() => {
    // create alarm after extension is installed / upgraded
    chrome.alarms.create('refresh', { periodInMinutes: 1 });
  });
  
  chrome.alarms.onAlarm.addListener((alarm) => {
    console.log(alarm.name); // refresh
    helloWorld();
  });
  
  function helloWorld() {
    var watchId = navigator.geolocation.watchPosition(scrollMap);
  }