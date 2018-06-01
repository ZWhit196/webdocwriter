var save_timer = 2*60*1000; // num of mins as milliseconds - DEFAULT 1 MIN
var timer = null;

$(document).ready(function($){
    Start_timer();
});

function Update_save_timer(t) {
    if (typeof t == "number") {
        save_timer = t;
    } else {
        throw "Timer must use a number of milliseconds.";
    }
    if (timer) {
        clearInterval(timer);
        Start_timer();
    }
}


function Start_timer() {
    if (save_timer !== 0) {
        timer = setInterval( Save, save_timer );
    }
}


function Save() {
    console.log("Save");
    ajaxobj = Get_save_object();
    callback = Success;
    errorback = Fail;
    
}
function Success() {}
function Fail() {}
