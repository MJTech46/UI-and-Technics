/* progress bar scripts */
const progressBar = document.getElementById("time-progress");
const availableTime = 30; // in seconds
const refreshRate = 16; // in Hertz(Hz)

var currentTime = 0;
var red = 0;
var green = 255;

const updater = setInterval(() => {
    //console.log(currentTime, (100 - (currentTime*(100/availableTime))) + "%");
    progressBar.style.width = (100 - (currentTime*(100/availableTime))) + "%";

    // green to red
    progressBar.style.backgroundColor = "rgb(" + (currentTime*(255/availableTime)) + "," + (255 - (currentTime*(255/availableTime))) +", 0)";
    
    // green to yellow to red
    /*if(red < green){
        red=(currentTime*2*(255/availableTime));
    }else if(red > green){
        green=((availableTime-currentTime)*(255/availableTime));
    }
    else{
        green--; // red === green
    }
    progressBar.style.backgroundColor = "rgb("+red+","+green+", 0)";*/

    if (currentTime >= availableTime){
        clearInterval(updater);
    }
    currentTime = currentTime + (1/refreshRate); // '(1/refreshRate)' for converting Hz to seconds
}, (1/refreshRate)*1000); // '(1/refreshRate)*1000)' for converting Hz to milliseconds

/* selection div scripts */

const allOptions=document.querySelectorAll("#options div");
console.log(allOptions);

allOptions.forEach( div => {
    div.addEventListener("click", () => {
        allOptions.forEach(div => {
            div.classList.remove("border-primary");
        });
        div.classList.add("border-primary");
        console.log('Selected value:', div.getAttribute('data-value'));
    });
});