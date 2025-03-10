function forgetpass(){

             document.getElementById('light').style.display = 'block';
           document.getElementById('fade').style.display = 'block';
}


function forgetpass1(a){
email1= String(document.getElementById('cemail').value);
     $.ajax({
          type: "POST",
          contentType: "application/json;charset=utf-8",
          url : '/resetpass',
          traditional: "true",
          data: email1,
          });
    console.log(a)
     if (a == 1){
         alert("Email Sent Successfully")
     }

}

function nouser(er){

    if (er == 0)
        email = document.getElementById("email")
        alert("No user found with email"+email)

}