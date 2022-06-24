"use strict"

const displaySharedEntries = () => {
    
    fetch("/get-shared-entries.json")
    .then((response) => response.json())
    .then((sharedEntries) => {
        const sharedEntriesContainer = document.querySelector('#shared-entries');
        let sharedEntryData = ''
        for (const entry of sharedEntries) {

             const entryDiv = `
                <div>
                    <h3><ul> 
                         <a id=${entry.prompt_week} href="/update-prompt-entry/${entry.prompt_week}">Week ${entry.prompt_week}</a> 
                          : ${entry.prompt}
                    </ul></h3> 
                    <li>
                        ${entry['entry']} <br>
                        ~ <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> 
                    </li>
                    <button class='view-entry' id="${entry.week}">View Entry</button>
                </div>`
            // const entryDiv = `
                
            //     <button type="button" class="collapsible"> Week ${entry.week} : ${entry.prompt} </button>
            //     <div class="content">
            //         <p>
            //             <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> : ${entry['entry']}
            //         </p>
            //     </div>`
                
            sharedEntryData += entryDiv
        }
        sharedEntriesContainer.innerHTML = sharedEntryData
    });
    
}
displaySharedEntries()

// const setUpCollapsiblePrompts = () => {
//     const coll = document.getElementsByClassName("collapsible");
//     let i;

//     for (i = 0; i < coll.length; i++) {
//         coll[i].addEventListener("click", function() {
//         this.classList.toggle("active");

//         const contents = document.querySelectorAll('div.content')
//         contents.forEach((content) => {
//     	    content.style.display = "none"
//         })

//         const content = this.nextElementSibling;
//         if (content.style.display === "block") {
//             content.style.display = "none";
//         } else {
//             content.style.display = "block";
//         }
//     });
//     }
// }
// setUpCollapsiblePrompts()
