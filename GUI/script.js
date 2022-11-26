const mic = document.getElementById("mic");
const micContainer = document.getElementById("mic-container");

// import python shell npm package
// import { PythonShell } from "python-shell";
// import { PythonShell } from './node_modules/python-shell/index';
// import { PythonShell } from './node_modules/python-shell/index.js';
const { PythonShell } = require("python-shell");
const path = require("path");

// add event listener to mic when window is loaded
window.addEventListener("load", () => {
  mic.addEventListener("click", () => {
    mic.classList.add("mic-active");
    mic.style.pointerEvents = "none";
    micContainer.classList.add("mic-container-active");

    var options = {
      scriptPath: path.join(__dirname, "../engine/"),
    //   pythonPath:
    //     "C:/Users/soumi/AppData/Local/Programs/Python/Python38/python.exe",
    };

    console.log(options.scriptPath);

    // var python = new PythonShell("voice.py", options);
    // python.on('message', function (message) {
    //     console.log(message);
    // });
    PythonShell.run("voice.py", options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      // console.log("results: %j", results);
      // display the result on screen in p tag
      document.getElementById("result").innerHTML = results[0];
      mic.classList.remove("mic-active");
      mic.style.pointerEvents = "auto";
      micContainer.classList.remove("mic-container-active");
    });

    // reset the result after 2 seconds
    setTimeout(() => {
      document.getElementById("result").innerHTML = "click the mic to activate the voice assistant";
    }, 2000);
  });
});
