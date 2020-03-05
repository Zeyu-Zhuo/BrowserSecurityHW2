var express = require("express");
var bodyParser = require('body-parser');
var app = express();
var dataToWrite;
var fs = require('fs');
var dataToWrite;
const port = 3000

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

app.post("/",function(req,res){
    dataToWrite = req.body.url + ','
    fs.appendFile('./out', dataToWrite, 'utf8', function (err) {});
    res.send();
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

app.get("/file",function(req,res){
    res.sendFile('/Users/zhuozeyu/CMU/BrowserSecurity/HW2/server/out');
})