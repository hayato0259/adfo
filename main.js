const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

app.on('window-all-closed', function () {
    app.quit();
});

app.on('ready', function () {
    var subpy = require('child_process').spawn('python', ['./resources/app/main.py']);
    var rq = require('request-promise');
    var mainAddr = 'http://localhost:5000/';

    var openWindow = function () {
        mainWindow = new BrowserWindow({
            frame: false,
            width: 1024,
            height: 640,
            backgroundColor: '#122738',
        });
        mainWindow.loadURL(mainAddr);
        // mainWindow.openDevTools();

        mainWindow.on('closed', function () {
            mainWindow = null;
            subpy.kill('SIGINT');
        });
    };

    var startUp = function () {
        rq(mainAddr)
            .then(function (htmlString) {
                openWindow();
            })
            .catch(function (err) {
                startUp();
            });
    };

    startUp();
});