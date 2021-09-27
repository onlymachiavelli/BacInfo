<?php
$hostname = "localhost";
$username = "root";
$password = "";

$connection = new mysqli($hostname, $username, $password, "eleve");


function findTarget($target){
    global $connection;
    $action = "SELECT * FROM users";
    $res = mysqli_query($connection, $action);
    while ($row = $res -> fetch_assoc()){
        if($row['cin'] == $target) {
            return TRUE;
        }
    }
    return FALSE;
}


if($connection) {
    
    if(findTarget("01447896325")) {
        print("it's here");
    }
    else {
        print("it does not exist !");
    }
}
else {
    print("Error conecting to DB");
}

?>