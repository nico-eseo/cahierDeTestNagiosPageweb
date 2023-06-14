document.addEventListener("DOMContentLoaded",function(event) {
    var form = document.getElementById("monFormulaire");


    var options = ["Test 1","Test 2","Test 3"];
    for (var i = 0; i < options.length; i++) {
        var label = document.createElement("label");
        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = "option";
        checkbox.value = options[i];
        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(options[i]));
        form.insertBefore(label,form.firstChild);
        form.insertBefore(document.createElement("br"),form.firstChild);
    }

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        
        var checkboxes = document.getElementsByName("option");
        var selectedOptions = [];
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedOptions.push(checkbox.value);
            }
        }) ;

        //requète ajax à écrire
    });
});