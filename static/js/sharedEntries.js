"use strict"

const setUpCollapsibleEntries = () => {
    const coll = document.getElementsByClassName("collapsible");
    

    for (const button of coll) {
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
        let entryDiv = ''
        let weeks = new Set()
        for (const entry of sharedEntries) {
            console.log("Week", entry.week);
            console.log("Name", entry.fname);

               
            if (!weeks.has(entry.week)) {
                sharedEntriesContainer.insertAdjacentHTML('beforeend', `
                <button id="${entry.week}" type="button" class="collapsible"> Week ${entry.week} : ${entry.prompt} </button>
                    <div id="entry_${entry.week}" class="content">
                        <p class=entry id="display_entry_text"> 
                            ${entry['entry']}
                            ~ <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> 
                        </p>
                    </div>`)

                weeks.add(entry.week)
                
            }
            else {
                console.log("ALREADY", weeks.has(entry.week))
                let collapsibleBtn = document.getElementById(`entry_${entry.week}`)
                collapsibleBtn.insertAdjacentHTML('beforeend',  
                
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
displaySharedEntries()
