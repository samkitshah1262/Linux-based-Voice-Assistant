// Modules to control application life and create native browser window
const {app, BrowserWindow, Menu, Tray, ipcMain, ipcRenderer} = require('electron')
const path = require('path')
const fs= require('fs')
function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: false,
    },
    autoHideMenuBar: true,
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')

  // minimize to tray on close
  mainWindow.on('close', function (event) {
    event.preventDefault();
    mainWindow.hide();
  });

  // tray functionalities
  let tray = null
  app.whenReady().then(() => {
    const iconPath = path.join(__dirname, 'assets/mic-outline2.png');
    tray = new Tray(iconPath);
    const contextMenu = Menu.buildFromTemplate([
        { label: 'Show App', click:  function(){
            mainWindow.show();
        } },
        { label: 'Quit', click:  function(){
          // before window closes, kill the python process
            // window.addEventListener("beforeunload", () => {
              fs.writeFile("./output.txt", "1", function (err) {
                if (err) throw err;
                console.log("Saved!");
              });
            // });
            mainWindow.destroy();
            app.quit();
        } }
    ]);

    tray.setToolTip('beetee')
    tray.setContextMenu(contextMenu)
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

