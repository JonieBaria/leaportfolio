const express = require("express");
const app = express();
const request = require("request")



app.use(express.static("static"));

app.get("/", function(req, res){
    res.send("Hello");
});

app.get("/home", function(req, res){
    res.sendFile(__dirname + "/index.html")

});

app.listen(process.env.PORT || 3000, function(){
    console.log("Server started on port 3000!")
});