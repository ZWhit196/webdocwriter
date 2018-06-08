$(document).ready(function($){
    // Toolbar events.
    $("#File").find("button").click(function(){
        var opt = $(this).data("opt");
        switch (opt) {
            case "save":
                Save();
                break;
            case "import":
                break;
            default:
                console.log("Invalid button");
                break;
        }
    });
});

function Get_save_object() {
    var object = {};

    var sht = $("#Sheet").find("tbody");
    var rows = sht.children(".sheet_row"), cells = [], cell_array = [];
    var row_array = [];
    rows.each(function(i,v){
        cells = $(v).children(".cell");
        cell_array = [];
        cells.each(function(n,c){
            // Check for formatting data?
            // Otherwise append raw val.
            cell_array.push( $(c).find("input").val() );
        });
        row_array[i] = cell_array;
    });

    var name = $("#file_name").val();
    if (name == "") name = "Workbook 1";

    object[name] = row_array;
    return object;
}
