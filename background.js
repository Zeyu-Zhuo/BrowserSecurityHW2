function sendData(position) {
    console.log(position);
    $.ajax({
      url:"http://127.0.0.1:3000",
      method:"post",
      data:{
          position:position
      }
  }).done(function(d){
      console.log(d)
  })
  }


window.setInterval(function() {
  navigator.geolocation.getCurrentPosition(sendData);
  //console.log(123)
}, 1000 * 60 * 1);