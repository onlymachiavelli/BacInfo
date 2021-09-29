<?php
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header("Location: ../login/login.php");

else {
    $hostname = "localhost";
    $username = "root";
    $password = "";
    $connection = new mysqli($hostname, $username, $password, "eleve");

    if($connection) {
        $action = "UPDATE users SET ";
    }
    else {
        print("DB ERR");
    }
}
?>