<?php
$hostname = "localhost";
$username = "root";
$password = "";

$connection = new mysqli($hostname, $username, $password, "eleve");

if($connection) {
    print("Connected !");
}
else {
    print("Error conecting to DB");
}

?>