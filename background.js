// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

// }); 

// chrome.tabs.onActivated.addListener(function(activeInfo) {
//  // how to fetch tab url using activeInfo.tabid
//  chrome.tabs.get(activeInfo.tabId, function(tab){
//     console.log(tab.url);
//  });
// }); 
titles = {};
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  if (changeInfo.title) {
    console.log(changeInfo.title)
    if (!titles[tabId]) {
      titles[tabId] = changeInfo.title
    } else if (titles[tabId] === changeInfo.title) {
      // do nothing
    } else { 
      chrome.tabs.query({}, function(tabs) {
        console.log(tabs)
        tabs.forEach(t => {
          if (t.id != tabId) {
            chrome.tabs.executeScript(t.id, {
              // hacky way to include jQuery
              file: 'jquery-3.4.1.min.js'
            }, function() {
              chrome.tabs.executeScript(t.id, 
                {code: `var title = "${changeInfo.title}"`}
              , function() {
                console.log(1234)
                chrome.tabs.executeScript(t.id, 
                  {file: 'insert_update.js'});
                })
           });
          }
        })
      });
    }
  }
}); 