"use strict"

const setUpCollapsibleEntries = () => {
    const coll = document.getElementsByClassName("collapsible");
    

    for (const button of coll) {
        console.log(button.id)
        button.addEventListener("click", function() {
        // this.classList.toggle("active");

        const contents = document.querySelectorAll('div.content')
        contents.forEach((content) => {
    	    content.style.display = "none"
        })

        // const content = this.nextElementSibling;
        const content= document.querySelector(`#entry_${button.id}`)
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
    }
}

const displaySharedEntries = () => {
    
    fetch("/get-shared-entries.json")
    .then((response) => response.json())
    .then((sharedEntries) => {
        const sharedEntriesContainer = document.querySelector('#shared-entries');
        let sharedEntryData = ''
        let currentWeek = 0
        for (const entry of sharedEntries) {

            //  const entryDiv = `
            //     <div>
            //         <h3> 
            //              <a id=${entry.prompt_week} href="/update-prompt-entry/${entry.prompt_week}">Week ${entry.prompt_week}</a> 
            //               : ${entry.prompt}
            //         </h3>
            //         <p class=entry id="display_entry_text"> 
            //             ${entry['entry']}
            //             ~ <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> 
            //         </p>
            //     </div>`
                // <button class='view-entry' id="${entry.week}">View Entry</button>
               
            
            const entryDiv = `
                
                <button id="${entry.week}" type="button" class="collapsible"> Week ${entry.week} : ${entry.prompt} </button>
                <div id="entry_${entry.week}" class="content">
                    <p class=entry id="display_entry_text"> 
                        ${entry['entry']}
                        ~ <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> 
                    </p>
                </div>`
                
            sharedEntryData += entryDiv
        }
        sharedEntriesContainer.innerHTML = sharedEntryData
        setUpCollapsibleEntries()
    });
    
}
displaySharedEntries()
