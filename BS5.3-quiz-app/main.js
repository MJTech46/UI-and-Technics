const progressBar = document.getElementById("time-progress");
const avilableTime = 10; // in seconds
const refreshRate = 16; // in Hertz(Hz)

var currentTime = 0;
const updater = setInterval(() => {
    //console.log(currentTime, (100 - (currentTime*(100/avilableTime))) + "%");
    progressBar.style.width = (100 - (currentTime*(100/avilableTime))) + "%";
    if (currentTime >= avilableTime){
        clearInterval(updater);
    }
    currentTime = currentTime + (1/refreshRate); // '(1/refreshRate)' for converting Hz to seconds
}, (1/refreshRate)*1000); // '(1/refreshRate)*1000)' for converting Hz to milliseconds