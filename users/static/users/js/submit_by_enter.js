var input = document.getElementById("login-form");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById('login-form').submit();
   return false;
  }
});