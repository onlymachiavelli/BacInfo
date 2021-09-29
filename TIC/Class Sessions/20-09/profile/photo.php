<?php
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');

else {
$hostname = "localhost";
$username = "root";
$password = "";
$connection = new mysqli($hostname, $username, $password, "eleve");


if ($connection){
    print("Connected !");
    


}
else {
    print ("OH NO !");
}
}
?>