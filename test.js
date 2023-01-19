fetch('http://194.87.62.91:8005/api/v1/send_message', {method: 'POST',headers: {'Content-Type': 'application/json',},body: JSON.stringify({ username: 'example' }),})


//
$.ajax({
  type: "POST",
  url: 'http://194.87.62.91:8005/api/v1/send_message',
  data: { username: 'example' },
  dataType: 'json'
});

$.post("http://194.87.62.91:8005/api/v1/send_message",{name: "Donald Duck"});


$('#createzaja').on('click', function(){
  $.post("https://kumicho.pw/api/v1/send_message",{name: "Donald Duck"});   
      })