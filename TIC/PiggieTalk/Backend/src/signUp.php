<?php

require ('connect.php');
require ('caesar.php');
require ('findUser.php');
connectDB();
define('shift', 3) ;

//data schema 

$password = caesar($_POST['password'], shift, TRUE);
$schema = array (
    "username" => $_POST['username'],
    "email " =>$_POST['email'],
    "name" => $_POST['fname'] . " " . $_POST['lname'],
    "birthday" => $_POST['date'],
    "password" => $passsword,
    "sex" => $_POST['sex'] 
);



?>