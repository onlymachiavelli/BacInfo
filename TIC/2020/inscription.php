<?php

mysql_connect("localhost", "root" , "" ) or die("Error connecting ");


mysql_select_db("2020") or die("Error  connecting ");

$id = $_POST["tel"] ;
$nom = $_POST["nom"] ;
$prenom = $_POST["prenom"] ;
$pass = $_POST["pass"] ;
$adr = $_POST["adresse"] ;
$check = "SELECT * FROM Client WHERE  Tel='$id' and Nom='$nom' and Prenom = '$prenom'";
$checkRes =  mysql_query($check) ;
if (mysql_num_rows($checkRes) > 0 ) {
    die ("Client est deja inscrit ! ") ;
}
else {
    
    $check = "SELECT * FROM Client WHERE Tel='$id'" ;
    if (mysql_num_rows($checkRes) > 0) {
        print("Erreur : Tel, Nom ou Prenom errone !");
    }
    else {
        $req = "insert into client values ('$id' , '$nom' , '$prenom' , '$adr' , '$pass' )" ;
        
        $checkRes = mysql_query($check) ;
        $res = mysql_query($req) ;
        if ($res) {
            print("Done saving the datas ") ;

        }
        else {
            die("error saving the datas ! " .mysql_error()) ;
        }
    }
}

mysql_close();



?>