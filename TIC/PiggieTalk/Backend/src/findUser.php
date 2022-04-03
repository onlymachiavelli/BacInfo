<?php
require ('connect.php');



function findUser($data) {
    connectDB();
    $req = "SELECT username FROM users WHERE username = '$data'";
    $res = query($req) ;
    return $res -> num_rows > 0 ? FALSE : TRUE ;
}
?>