var save_timer = 0; // Millisecond timer

$(document).ready(function($){
    if (save_timer != 0) {
        setInterval( Save, save_timer );
    }
});

function Update_save_timer() {
    console.log("Updated save timer.");
}

function Save() {
    console.log("Save");
}