var express = require("express");
var bodyParser = require('body-parser');//解析,用req.body获取post参数
var app = express();
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({extended: false}));

app.post("/",function(req,res){
    console.log(JSON.stringify(req.body));
    res.send({hello:'world'});
})

app.listen(3000, () => console.log(`Example app listening on port ${3000}!`))