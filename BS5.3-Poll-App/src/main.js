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
mainBodyElement.style.paddingTop = `${navHeight + 15}px`;
