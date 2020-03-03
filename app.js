var express = require("express");
var bodyParser = require('body-parser');
var app = express();

const port = 3000

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

app.post("/",function(req,res){
    console.log(JSON.stringify(req.body));
    res.send({hello:'world'});
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))