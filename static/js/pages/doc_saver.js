var save_timer = 2*60*1000; // num of mins as milliseconds - DEFAULT 2 MIN
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
    SetAjaxArgs(Get_save_object(), Success_func, Fail_func);
    AjaxCall();
}

function Success_func(data) {
    console.log("Saved!",data);
}

function Fail_func() {
    console.log("There was a problem...");
}
