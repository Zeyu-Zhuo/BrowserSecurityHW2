// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

// }); 

chrome.tabs.onActivated.addListener(function(activeInfo) {
 // how to fetch tab url using activeInfo.tabid
 chrome.tabs.get(activeInfo.tabId, function(tab){
    console.log(tab.url);
    $.ajax({
      url:"http://127.0.0.1:3000",
      method:"post",
      data:{
          url:tab.url
      }
  }).done(function(d){
      console.log(d)
  })
 });
}); 

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  if(changeInfo.url){
    console.log(changeInfo.url);
    $.ajax({
      url:"http://127.0.0.1:3000",
      method:"post",
      data:{
          url:changeInfo.url
      }
  }).done(function(d){
      console.log(d)
  })
  }
  //console.log(tab.url)
}); 