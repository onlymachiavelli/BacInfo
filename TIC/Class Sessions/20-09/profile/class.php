<?php
session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header("Location: ../login/login.php");

else {
    $hostname = "localhost";
    $username = "root";
    $password = "";
    $connection = new mysqli($hostname, $username, $password, "eleve");

    if($connection) {
        $action = "UPDATE users SET class = '".$_POST['userclass']."' WHERE cin = '".$_SESSION['user']."'";
        if($connection -> query($action)) {
            header("Location: profile.php");
        }
        else die (mysqli_error($connection));
    }

    else {
        print("DB ERR");
    }
}
?>