"use strict"

const setUpCollapsiblePrompts = () => {
    const acc = document.getElementsByClassName("collapsible");
    

    for (const button of acc) {
        console.log("button", button)
        button.addEventListener("click", function() {
        // this.classList.toggle("active");

        const contents = document.querySelectorAll('div.content')
        contents.forEach((content) => {
    	    content.style.display = "none"
        })

        // const content = this.nextElementSibling;
        const contentPrompt= document.querySelector(`#entry_${button.id}`)
        console.log("***contentPrompt", contentPrompt)
        if (contentPrompt.style.display === "block") {
            contentPrompt.style.display = "none";
        } else {
            contentPrompt.style.display = "block";
        }
    });
    }
}

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
                promptData +=`
                <button id="${prompt.week}" type="button" class="collapsible" style="background-color: #FFF5EE; color: black" > Week ${prompt.week} : ${prompt.prompt} </button>
                <div id="entry_${prompt.week}" class="content">
                    <button style="background-color: #FFF5EE;" onclick="location.href='/update-prompt-entry/${prompt.week}'">Create Entry</button>
                </div>`
            } else {
                promptData +=
                `<button id="${prompt.week}" type="button" class="collapsible"> Week ${prompt.week} : ${prompt.prompt} </button>
                <div id="entry_${prompt.week}" class="content">
                    <p id="display_entry_text">  ${prompt.entry}</p>
                    <button style="background-color: #FFF5EE;" onclick="location.href='/update-prompt-entry/${prompt.week}'">Edit Entry</button>
                </div>`
            } 
        }
        promptsContainer.innerHTML = promptData
        setUpCollapsiblePrompts()
    }); 
}
displayPrompts()
