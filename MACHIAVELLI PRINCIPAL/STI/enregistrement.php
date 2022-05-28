<?php
mysql_connect("localhost" , "root" , "") or die ("Error connecting ! ") ;
mysql_select_db("SWNUM") or die ("error selecting db ! ") ;



$id = $_POST["permis"] ;

$check = "SELECT * FROM testeur WHERE numPermis='$id'";
$rescheck=mysql_query($check) ;
if (mysql_num_rows($rescheck) > 0) {
    die ("User already exists ! "); 

} 
else {

    $sex=  $_POST["sex"] ;
    $nom = $_POST["nom"] ;
    $prenom= $_POST["prenom"] ;
    $req = "INSERT INTO testeur VALUES ('$id','$nom','$prenom','$sex')" ;
    $res = mysql_query($req) ;
    if ($res) {
        print("done saving the datas !") ;
    }
    else {
        die(mysql_error());
    }
}

?>