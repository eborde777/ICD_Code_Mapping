exports.CreateTableFromJSON = function(my_records){

    var col = []; //list to collect keys

    // extracting table headers
    for(var i=0; i<my_records.length; i++){
        for(var key in my_records[i]){
            if(col.indexOf(key) === -1){
                col.push(key)
            }
        }
    }

    // Creating table
    var table = document.createElement("table");
    table.setAttribute('class', 'table table-hover');

    // creating dynamic row for the headers
    var tr = table.insertRow(-1);

    for (var i =0; i < col.length; i++){
        var th = document.createElement("th"); // Table Header
        th.innerText = col[i];
        tr.appendChild(th);
    }

    // Adding json data to the table as rows
    for (var i=0; i<my_records.length; i++){
        tr = table.insertRow(-1); // ROW

        for (var j=0; j< col.length; j++){
            var tabCell = tr.insertCell(-1); // Cell
            tabCell.innerHTML = my_records[i][col[j]] // like [0,0] [0,1]
        }
    }

    // Appending the table to the div element
    var divContainer = document.getElementById("showData"); // fetching element with this id
    divContainer.innerHTML = " ";
    divContainer.appendChild(table);

};
