<?php
session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');



else {
    $hostname = "localhost";
    $username = "root";
    $password = "";
    $connection = new mysqli($hostname, $username, $password, "eleve");

    if($connection){
        print("CONNECTED !");

    }
    else print("ERR CONNECTING TO DB !");
}


function getTarget($cin, $target){
    global $connection;
    $action = "SELECT".$target." FROM users"; 
    $res = mysqli_query($connection, $action);

}
?>



<!DOCTYPE html>
<html>

    <head>
        <link rel="stylesheet" href="" />
        <?php //echo("<title>".getTarget($_SESSION['cin'])."</title>") ;?>
    </head>
    <body>
        <header></header>

    </body>
</html>