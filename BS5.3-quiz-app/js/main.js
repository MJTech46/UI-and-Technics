const progressBar = document.getElementById("time-progress");
const avilableTime = 10; // in seconds
const refreshRate = 16; // in Hertz(Hz)

var currentTime = 0;
var red = 0;
var green = 255;

const updater = setInterval(() => {
    //console.log(currentTime, (100 - (currentTime*(100/avilableTime))) + "%");
    progressBar.style.width = (100 - (currentTime*(100/avilableTime))) + "%";

    // green to red
    progressBar.style.backgroundColor = "rgb(" + (currentTime*(255/avilableTime)) + "," + (255 - (currentTime*(255/avilableTime))) +", 0)";
    
    // green to yellow to red
    /*if(red < green){
        red=(currentTime*2*(255/avilableTime));
    }else if(red > green){
        green=((avilableTime-currentTime)*(255/avilableTime));
    }
    else{
        green--; // red === green
    }
    progressBar.style.backgroundColor = "rgb("+red+","+green+", 0)";*/

    if (currentTime >= avilableTime){
        clearInterval(updater);
    }
    currentTime = currentTime + (1/refreshRate); // '(1/refreshRate)' for converting Hz to seconds
}, (1/refreshRate)*1000); // '(1/refreshRate)*1000)' for converting Hz to milliseconds