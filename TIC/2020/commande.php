<?php

mysql_connect("localhost", "root" , "" ) or die("Error connecting ");
mysql_select_db("2020") or die("Error  connecting ");


$id = $_POST["tel"] ;
$pass = $_POST["pass"];
$authRreq = "SELECT * FROM Client WHERE Tel='$id' AND MotPass = '$pass'" ;
$auth = mysql_query($authRreq) ;

if (mysql_num_rows($auth) === 0 ) {
    die ("user is not authed ") ;

}
else {
     $date = date("Y-m-d h:i:s") ;
    $pizza = $_POST["pizza"] ;

    $qte = $_POST["qte"] ;
    $req = "INSERT INTO commande VALUES ('$pizza', '$id', '$date' , '$qte')";
    $res = mysql_query($req) ;
    if ($res) {
        echo "operation reussie" ;

    }
    else {
        die ("Erreur ! ") ;
    }
}





?>