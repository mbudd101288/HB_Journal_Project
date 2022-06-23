"use strict"

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

            if (prompt.entry === null) {
                promptData +=
                `<div>
                    <p>Week ${prompt['week']}: ${prompt['prompt']}</p>
                    <button onclick="location.href='/update-prompt-entry/${prompt['week']}'">Create Entry</button>
                </div>`
            } else {
                promptData +=
                `<div>
                    <p>Week ${prompt['week']}: ${prompt['prompt']}</p>
                    <button onclick="location.href='/update-prompt-entry/${prompt['week']}'">Edit Entry</button>
                </div>`
            } 
        }
        promptsContainer.innerHTML = promptData
    }); 
}
displayPrompts()
