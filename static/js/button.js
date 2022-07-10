


const entryBtn = document.querySelector("#entry_button");
entryBtn.addEventListener('click', (evt) => {
    const entryInput = document.querySelector('textarea[name="entry"]');
    if (entryInput.value.length<1) {
        evt.preventDefault();
        alert("Please enter text to save an entry 🤗")
        }
    })


const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

