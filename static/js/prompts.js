"use script"

const displayPrompts = () => {

    fetch("/get-user-entries.json")
    .then((response) => response.json())
    .then((prompts) => {
        const promptsContainer = document.querySelector('#user-prompts');
        let promptData = ''
        for (const prompt of prompts) {
            // const promptDiv = document.createElement("div");
            // promptDiv.class = 'card'
            // const promptDescription = document.createElement("p");
            // promptDescription.innerHTML = `Week ${prompt['week']} : ${prompt['prompt']}`;
            // const createPromptEntryButton = document.createElement("button")
            // createPromptEntryButton.innerHTML = "Create Entry"
            // createPromptEntryButton.id = prompt['week']
            // createPromptEntryButton.class = 'create-entry'
            // promptDiv.appendChild(promptDescription)
            // promptDiv.appendChild(createPromptEntryButton)
            // promptsContainer.appendChild(promptDiv)

            // do this instead

            //turn into expanding list? or if else 
            const promptDiv = `
                <div>

                    <p>Week ${prompt['week']}: ${prompt['prompt']}</p>
                    <button class='create-entry' id="${prompt.week}">Create Entry</button>
    
                    <<button class='edit-entry' id="${prompt.week}">Edit Entry</button>
    
                </div>
            `
            
            promptData += promptDiv
        }
        promptsContainer.innerHTML = promptData
    });
    
}
displayPrompts()

// const createEntryButton = document.querySelector("button.create-entry");

// function createEntry () {


// create event handler for button for entry<week> route - use the class for query selector - use the id to give to the route