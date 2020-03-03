// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

// }); 

chrome.tabs.onActivated.addListener(function(activeInfo) {
 // how to fetch tab url using activeInfo.tabid
 chrome.tabs.get(activeInfo.tabId, function(tab){
    console.log(tab.url);
 });
}); 

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  if(changeInfo.url){
    console.log(changeInfo.url);
  }
  //console.log(tab.url)
}); 