


const entryBtn = document.querySelector("#entry_button");
entryBtn.addEventListener('click', (evt) => {
    const entryInput = document.querySelector('textarea[name="entry"]');
    if (entryInput.value.length<1) {
        evt.preventDefault();
        alert("Please enter text to save an entry 🤗")
        }
    })




// const editBtn = document.querySelector("#edit_entry_button");
// entryBtn.addEventListener('click', (evt) => {
//     const entryInput = document.querySelector('textarea[name="entry"]');
//     if (entryInput.value.length<1) {
//         evt.preventDefault();
//         alert("Please enter text to save an entry 🤗")
//         }
//     })


const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
