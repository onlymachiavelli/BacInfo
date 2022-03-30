<?php
    include 'connect/mySQLAuth.php';
    include 'services/postData.php';
    connect("root", "", "piggieTalk");
    $datas = array(
        "username" => $_POST["username"],
        "fullname" => $_POST["fname"]." ".$_POST["lname"],
        "email" => $_POST["email"],
        "password" => $_POST["password"],
        "birthday" => $_POST["birthday"],
        "sex" =>$_POST['sex']
    );

    postData($datas, "piggieTalk","../../../Front/index.html") ;
    
?>