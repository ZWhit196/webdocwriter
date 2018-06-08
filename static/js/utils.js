var ajaxobj = {}, callback = Generic_callback, errorback = Generic_error;


function SetAjaxArgs(o, c, e) { ajaxobj = o; callback = c; errorback = e; }

function NullAjaxArgs() { ajaxobj = null; callback = null; errorback = null; }

function AjaxCall() {
    $.ajax({
        url: window.location,
        method: 'POST',
        data: JSON.stringify( ajaxobj ),
        contentType: 'application/json'
    }).done(function(dt) {
        callback(dt);
        NullAjaxArgs(); // move to `.always`
    });
}

function IsInArray(target, array) {
    if( array.indexOf(target)>-1 ) return true;
    return false;
}

function TogglePassField(el) {
    var prop = ( $(el).prop("type")=="password" )?"text":"password";
    $(el).prop( "type", prop );
}

function Generic_callback() {
    console.log("Generic success callback.");
}

function Generic_error() {
    console.log("An error occurred.");
}