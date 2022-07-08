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
        
          });
      });





const setUpCollapsibleEntries = () => {
    const coll = document.getElementsByClassName("collapsible");
    

    for (const button of coll) {
        button.addEventListener("click", function() {

        // const contents = document.querySelectorAll('div.content')
        // contents.forEach((content) => {
    	//     content.style.display = "none"
        // })

        const content= document.querySelector("#user_entry_coll")
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
    }
}

setUpCollapsibleEntries()
