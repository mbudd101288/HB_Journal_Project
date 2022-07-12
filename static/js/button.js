"use strict"

const entryBtn = document.querySelector("#entry_button");
entryBtn.addEventListener('click', (evt) => {
    const entryInput = document.querySelector('textarea[name="entry"]');
    if (entryInput.value.length<1) {
        evt.preventDefault();
        alert("Please enter text to save an entry 🤗")
        }
    })

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Allows users to tab in text area - consider not using this? makes it more difficult for user's that don't use a mouse
var textareas = document.getElementsByTagName('textarea');
var count = textareas.length;
for(var i=0;i<count;i++){
    textareas[i].onkeydown = function(e){
        if(e.keyCode===9 || e.which===9){
            e.preventDefault();
            var s = this.selectionStart;
            this.value = this.value.substring(0,this.selectionStart) + "\t" + this.value.substring(this.selectionEnd);
            this.selectionEnd = s+1; 
        }
    }
}