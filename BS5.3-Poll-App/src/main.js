// Toggling the theme
const modeButton = document.getElementById("modeButton");
const htmlElement = document.querySelector("html");
const themeColor = localStorage.getItem("themeColor");

// To loading the data from the localstorage
if(themeColor === "dark"){
    htmlElement.dataset.bsTheme = "dark";
} else {
    htmlElement.dataset.bsTheme = "light";
}

modeButton.addEventListener("click", () => {
    if (htmlElement.dataset.bsTheme === "light") {
        htmlElement.dataset.bsTheme = "dark";
        localStorage.setItem("themeColor", "dark");
    } else {
        htmlElement.dataset.bsTheme = "light";
        localStorage.setItem("themeColor", "light")
    }
});

//Adding accurate padding
const navElement = document.querySelector("nav"); 
const mainBodyElement = document.getElementById("mainBody");
const navHeight = navElement.offsetHeight;
//mainBodyElement.style.paddingTop = `${navHeight + 15}px`;

// for createPoll page
const addOptionBtn = document.getElementById("addOption");
const deleteOptionBtn = document.getElementById("deleteOption");
const optionsDiv = document.getElementById("options");
const optionsCountInput = document.getElementById("optionsCount");
var optionCounter = 2;
optionsCountInput.value = optionCounter;
console.log(optionsCountInput.value)

addOptionBtn.addEventListener("click", () => {
    // Create a new input element
    const newInput = document.createElement("input");
    newInput.id = `answerOptions${optionCounter + 1}`; // Increment the ID for each new option
    newInput.type = "text";
    newInput.className = "form-control mb-3";
    newInput.placeholder = `Option ${optionCounter + 1}`;
    newInput.required = true;
    // Append the new input element to the optionsDiv
    optionsDiv.appendChild(newInput);
    // Increment the optionCounter
    optionCounter++;
    optionsCountInput.value = optionCounter;
    console.log("Added:",optionsCountInput.value)

    if (optionCounter > 2) {
        deleteOptionBtn.hidden = false;
    } else {
        deleteOptionBtn.hidden = true;
    }
});

deleteOptionBtn.addEventListener("click", () =>{
    const lastInput = document.getElementById(`answerOptions${optionCounter}`);
    if (optionCounter > 2) {
        lastInput.remove();
        optionCounter--;
        optionsCountInput.value = optionCounter;
        console.log("Removed:", optionsCountInput.value)
    }
    if (optionCounter === 2) {
        deleteOptionBtn.hidden = true;
    }
     
});
