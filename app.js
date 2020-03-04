var express = require("express");
var bodyParser = require('body-parser');//解析,用req.body获取post参数
var app = express();
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({extended: false}));

    app.use(function(req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept","key");
        next();
    });


app.get("/",function(req,res){
    //console.log(JSON.stringify(req));
    console.log(req.query)
    res.send();
})

app.listen(3000, () => console.log(`Example app listening on port ${3000}!`))
