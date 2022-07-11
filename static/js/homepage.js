"use strict";

let i = 0;
let txt = '52 Weeks of Journal Intentions'; /* The text */
const speed = 150; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("login_title").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

typeWriter()


const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

// THE MOST IMPORTANT LINE you should add when using a background video
//  * HTML5 videos will "steal" the click event from other elements.
//  * Preventing the default action will disable click events for the video.

document.querySelector('.background-video video').addEventListener(
  'click',
  e => e.preventDefault()
);

// Callback function to scale the video so that it covers the entire screen
function scaleVideo() {
  const innerWidth = window.innerWidth;
  const innerHeight = window.innerHeight;
  if (innerWidth > innerHeight) {
    document.querySelector('.background-video video').setAttribute('width', innerWidth);
    document.querySelector('.background-video video').setAttribute('height', '');
  } else {
    document.querySelector('.background-video video').setAttribute('height', innerHeight);
    document.querySelector('.background-video video').setAttribute('width', '');
  }
  const videoHeight = getComputedStyle(document.querySelector('.background-video video')).height;
  document.querySelector('header').style.height = videoHeight;

}

// // Caveat: this causes the page to look wonky on initial load.
window.onload = scaleVideo;

// // Resize the video if the window is resized
window.onresize = scaleVideo;



