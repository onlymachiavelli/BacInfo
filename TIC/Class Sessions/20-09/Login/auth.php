<?php
$servername = "localhost";
$userame = "root";
$password = "";
$connection = new mysqli($servername, $userame, $password, "eleve");

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
    if(makeAuth($_POST['cin'], $_POST['pass'])) print ("authorized");
    else print("unauthorized");
}
else {
    die ("Error Connecting to DB");
}

?>