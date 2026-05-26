function get_otp() {
    var otp = prompt("Please enter The otp sent to your mail");
  
  }
  
  var email = ''
  
  function  otp_window() {

    email= String(document.getElementById('email3').value);
         $.ajax({
            type: "POST",
            contentType: "application/json;charset=utf-8",
            url : '/send_otp',
            traditional: "true",
            data: email,
            });
            document.getElementById('light').style.display = 'block';
            document.getElementById('fade').style.display = 'block';
      }
  
  
  verified = () => {
      document.getElementById("resend1").disabled=true;
      otp = ''
      otp1 = document.getElementById('otp1').value;
      email = document.getElementById('email3').value;
      fetch('/verified', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, otp: otp1 })
      })
        .then(response => response.json())
        .then(data => {
          if (data.result.status === 'success') {
            console.log(data);
            alert("Verified Successfully please login to continue")
            window.location.href = "/";
            // Place any code here that relies on the 'otp' value
          } else {
            alert('Invalid OTP please try again');
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
      
  
  }
  let timerOn = true;
  
  function timer(remaining) {
      document.getElementById('timer1').style.display  ='block';
    var m = Math.floor(remaining / 60);
    var s = remaining % 60;
  
    m = m < 10 ? '0' + m : m;
    s = s < 10 ? '0' + s : s;
    document.getElementById('timer').innerHTML = m + ':' + s;
    remaining -= 1;
  
    if(remaining >= 0 && timerOn) {
      setTimeout(function() {
          // if(remaining==1){
          //     document.getElementById("resend1").disabled=false;
          //     document.getElementById('timer1').style.display  ='none';
          // }
          timer(remaining);
      }, 1000);
      return;
    }
  document.getElementById("resend1").disabled=false;
  document.getElementById('timer1').style.display  ='none';
    if(!timerOn) {
      // Do validate stuff here
      return;
    }
  
  
  }
  
  resend = () => {
       $.ajax({
          type: "POST",
          contentType: "application/json;charset=utf-8",
          url: '/send_otp',
          traditional: "true",
          data: email,
  
      });
       document.getElementById('timer1').style.display  ='none';
       document.getElementById("resend1").disabled=true;
       timer(60);
  }