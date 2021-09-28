<?php
session_start();


$hostname = "localhost";
$userame = "root";
$password = "";
$connection = new mysqli($hostname, $userame, $password, "eleve");

function makeAuth($username, $password){
    global $connection;
    $authquery = "SELECT * FROM users";
    $res = mysqli_query($connection, $authquery);
    while ($row = $res -> fetch_assoc()){
        if ($row['cin'] == $username && $row['password'] == $password) {
            return TRUE;
        }
    }
    return FALSE;
}


if ($connection) {
    if(makeAuth($_POST['cin'], $_POST['pass'])){
        print ("authorized");
        $_SESSION['user'] = $_POST['cin'];
        $_SESSION['pass'] = $_POST['pass'];
        header("Location: ../profile/profile.php");
    }
    else print("unauthorized");
}
else {
    die ("Error Connecting to DB");
}

?>