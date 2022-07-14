"use strict"

const followBtn = document.querySelector('#follow_button');
followBtn.addEventListener('click', (evt) => {
        evt.preventDefault();
      
        const formInputs = {
          friend: window.location.href.split('/')[4]
        };
      
        fetch('/update_following', {
          method: 'POST',
          body: JSON.stringify(formInputs),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((responseJson) => {
            alert(responseJson.follow_msg);
            followBtn.innerHTML = responseJson.button_text
        
            if (responseJson.button_text === "Unfollow") {
                followBtn.innerHTML = `
                <span><img id="unfollow" src="/static/images/unfriend_icon.png" alt="unfriend img"></span>
                `
            }
            else if (responseJson.button_text ==="Follow") {
                followBtn.innerHTML = ` 
                     <span><img id="follow" src="/static/images/friend_icon.png" alt="friend img"></span>
                     `
            }
          });
      });


const setUpCollapsibleEntries = () => {
    const coll = document.getElementsByClassName("collapsible");
    

    for (const button of coll) {
        button.addEventListener("click", function() {

        const contents = document.querySelectorAll('div.content')
        contents.forEach((content) => {
    	    content.style.display = "none"
        })

        const content= document.querySelector(`#entry_${button.id}`)
        
        if (content.style.display === "block") {
            console.log("Is this working?")
            content.style.display = "none";
        } else {
            console.log("Mayybe not working?")
            content.style.display = "block";
        }
    });
    }
}

setUpCollapsibleEntries()

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

