let i = 0;
let txt = '52 Weeks of Journal Intentions'; /* The text */
const speed = 200; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("login_title").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

typeWriter()