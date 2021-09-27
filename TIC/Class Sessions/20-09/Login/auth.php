<?php
$servername = "localhost";
$userame = "root";
$password = "";
$connection = new mysqli($servername, $userame, $password, "eleve");

function makeAuth($username, $password){
    return 0;
}


if ($connection) {
    print("Connected to DB");

}
else {
    die ("Error Connecting to DB");
}

?>