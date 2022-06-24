


const entryBtn = document.querySelector("#entry_button");
entryBtn.addEventListener('click', (evt) => {
    const entryInput = document.querySelector('textarea[name="entry"]');
    if (entryInput.value.length<1) {
        evt.preventDefault();
        alert("Please enter text to save an entry 🤗")
        }
    })


const coll = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");

    const contents = document.querySelectorAll('div.content')
    contents.forEach((content) => {
    	content.style.display = "none"
    })

    const content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
