var dynamic_table = require('./dynamic_table');
var {PythonShell} = require('python-shell');


function myfunc() {
            var x = document.getElementById('icd_input').value;
            load_data(x)
}

function load_data(data) {
    let options = {
                  mode: 'text',
                  args: data
                };

    PythonShell.run('backend.py', options, function (err, results) {
      if (err) throw err;
      // progressBar();
      console.log(JSON.parse(results));
      dynamic_table.CreateTableFromJSON(JSON.parse(results));


      console.log('finished');
    });

}

// function progressBar(){
//     var elem = document.getElementById("myBar");
//               var width = 1;
//               var id = setInterval(frame, 10);
//
//               function frame() {
//                 if (width >= 100) {
//                   clearInterval(id);
//                 } else {
//                   width++;
//                   elem.style.width = width + '%';
//                   elem.innerHTML = width * 1  + '%';
//                 }
//               }
// }
