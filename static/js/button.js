


const entryBtn = document.querySelector("#entry_button");
entryBtn.addEventListener('click', (evt) => {
    const entryInput = document.querySelector('textarea[name="entry"]');
    if (entryInput.value.length<1) {
        evt.preventDefault();
        alert("Please enter text to save an entry 🤗")
        }
    })



const followBtn = document.querySelector('#follow_button');
followBtn.addEventListener('click', (evt) => {
        evt.preventDefault();
      
        const formInputs = {
          friend: Yes,
        };
      
        fetch('/start_following', {
          method: 'POST',
          body: JSON.stringify(formInputs),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((responseJson) => {
            alert(responseJson.status);
          });
      });

// const editBtn = document.querySelector("#edit_entry_button");
// entryBtn.addEventListener('click', (evt) => {
//     const entryInput = document.querySelector('textarea[name="entry"]');
//     if (entryInput.value.length<1) {
//         evt.preventDefault();
//         alert("Please enter text to save an entry 🤗")
//         }
//     })


const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))