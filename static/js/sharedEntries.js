"use script"

const displaySharedEntries = () => {

    fetch("/get-shared-entries.json")
    .then((response) => response.json())
    .then((sharedEntries) => {
        const sharedEntriesContainer = document.querySelector('#shared-entries');
        let sharedEntryData = ''
        for (const entry of sharedEntries) {
        
            const entryDiv = `
                <div>
                    <h3> 
                        <a id=${entry.user_id} href="/entry/${entry.user_id}">${entry.fname}</a> : Week ${entry.prompt}
                    </h3> <br> 
                    <p>
                        ${entry['entry']}
                    </p>
                    <button class='view-entry' id="${entry.week}">View Entry</button>
                </div>
            `
            
            sharedEntryData += entryDiv
        }
        sharedEntriesContainer.innerHTML = sharedEntryData
    });
    
}
displaySharedEntries()