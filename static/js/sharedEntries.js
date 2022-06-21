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
                    <p> ${entry['fname']}: ${entry['entry'].slice(0,100)}</p>
                    
                    <button class='view-entry' id="${entry.week}">View Entry</button>
    
                </div>
            `
            
            sharedEntryData += entryDiv
        }
        sharedEntriesContainer.innerHTML = sharedEntryData
    });
    
}
displaySharedEntries()