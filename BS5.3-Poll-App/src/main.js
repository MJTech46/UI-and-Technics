// Toggling the theme
const modeButton = document.getElementById("modeButton");
const htmlElement = document.querySelector("html");
modeButton.addEventListener("click", () => {
    if (htmlElement.dataset.bsTheme === "light") {
        htmlElement.dataset.bsTheme = "dark";
    } else {
        htmlElement.dataset.bsTheme = "light";
    }
});

//Adding accurate padding
const navElement = document.querySelector("nav"); 
const mainBodyElement = document.getElementById("mainBody");
const navHeight = navElement.offsetHeight;
mainBodyElement.style.paddingTop = `${navHeight + 15}px`;
