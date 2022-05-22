<?php

mysql_connect("localhost", "root" , "" ) or die("Error connecting ");


mysql_select_db("2020") or die("Error  connecting ");

 $id = $_POST["tel"] ;
$check = "select * from client where Tel='$id'" ;
$checkRes mysql_query($check) ;
if (mysql_num_rows($checkRes) >0 ) {
    die("Erreur : Tél, Nom ou Prénom erroné !")
}
else {
    
    $nom = $_POST["nom"] ;
    $prenom = $_POST["prenom"] ;
    $pass = $_POST["pass"] ;
    $adr = $_POST["adresse"] ;
    $check = "select * from client where Tel='$id' and Nom = '$nom' and Prenom = '$prenom'" ;
    $checkRes mysql_query($check) ;
    if (mysql_num_rows($checkRes) >0) {
        die ("Client est deja inscrit ! ") ;
    }
    else {
        $req = "insert into client values ('$tel' , '$nom' , '$prenom' , '$adr' , '$pass' )" ;

        $res = mysql_query($res) ;
        if ($res) {
            print("Done saving the datas ") ;

        }
        else {
            die("error saving the datas ! ") ;
        }
    }
}

mysql_close();



?>