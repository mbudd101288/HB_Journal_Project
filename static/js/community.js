"use strict"

const radios = document.querySelectorAll('input')
for (const radio of radios) {
  radio.onclick = (e) => {
    console.log(e.target.value);
    displaySharedEntries(e.target.value);
  }
}

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
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
    }
}

const displaySharedEntries = (isEveryone) => {
    
    const url = `/get-shared-entries.json?communityView=${isEveryone}`
    fetch(url)
    .then((response) => response.json())
    .then((sharedEntries) => {
        let sharedEntriesContainer = document.querySelector('#shared-entries');
        sharedEntriesContainer.innerHTML = ''
        let entryDiv = ''
        let weeks = new Set()
        for (const entry of sharedEntries) {
            console.log("Week", entry.week);
            console.log("Name", entry.fname);

               
            if (!weeks.has(entry.week)) {
                sharedEntriesContainer.insertAdjacentHTML('beforeend', `
                <button id="${entry.week}" type="button" class="collapsible complete-entry"> Week ${entry.week} : ${entry.prompt} </button>
                    <div id="entry_${entry.week}" class="content">
                        <p class=entry id="display_entry_text"> 
                            ${entry['entry']}
                            ~ <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> 
                        </p>
                    </div>`)

                weeks.add(entry.week)
                
            }
            else {
                let collapsibleDiv = document.getElementById(`entry_${entry.week}`)
                collapsibleDiv.insertAdjacentHTML('beforeend',  
                
                    `<p class=entry id="display_entry_text"> 
                        ${entry['entry']}
                        ~ <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> 
                    </p>`
                )
            }  
    
        }
        setUpCollapsibleEntries()
    });
    
}
displaySharedEntries(true)
