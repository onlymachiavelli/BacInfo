<?php

if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['nc']) && isset($_POST['sex'])) {
    $localhost = "localhost";
    $username = "root";
    $password = "";
    mysql_connect($localhost,$username,$password) or die("Error connecting to phpMyadmin");
    mysql_select_db("formation") or die("Error selecting the database") ;
    $fullname = $_POST['name']; 

    $name = substr($fullname, 0 , strpos($fullname, " "));
    $lname = substr($fullname , strpos($fullname, " ") +1 , strlen($fullname)) ;
    $reqDatas = array(
        "name" =>$name, 
        "lname" =>$lname,
        "sex" =>$_POST['sex'],
        "email" =>$_POST['email'],
        "bac" =>$_POST['nc'],
    );
    $req = "INSERT INTO CONDIDAT (nom,prenom,genre,email,bac) VALUES ('".$reqDatas['name']."','".$reqDatas['lname']."','".$reqDatas['sex']."','".$reqDatas['email']."','".$reqDatas['bac']."')";
    $res = mysql_query($req) ;
    if (mysql_affected_rows() >0 ) {
        echo "Done saving datas ! "; 
    }
    else {
        echo "Error saving datas ! perhpas there's an error !";
        echo "<br/> " . mysql_error() ;
    }
    echo "<br/> <a href='index.html'>Goo back</a>";
}
else {
    echo "Error Getting datas ! You must fill all the fields !";
}

?>
