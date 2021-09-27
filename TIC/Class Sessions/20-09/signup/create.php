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
    if(findTarget($_POST['cin'])) {
        print("Used CIN !");
    }
    else {
        $gethob= "000";
        if ($_POST['music']) $gethob[0]  = "1" ;
        else $gethob[0]  = "0" ;


        if ($_POST['internet']) $gethob[1]  = "1" ;
        else $gethob[1]  = "0" ;


        if ($_POST['photograph']) $gethob[2]  = "1" ;
        else $gethob[2]  = "0" ;

        $mysql = "INSERT INTO users (fullname, cin, date, password, gender, email, phone , adress, hobb) values ('".$_POST['lname']."', '".$_POST['cin']."', '".$_POST['date']."','".$_POST['pass']."','".$_POST['gender']."','".$_POST['email']."','".$_POST['phone']."','".$_POST['adress']."','".$gethob."')";

        if ($connection -> query($mysql)){
            print("ADDED TO YOUR DATABASE !");
        }
        else {
            die(mysqli_error($connection));
        }
    }
}
else {
    print("Error conecting to DB");
}

?>