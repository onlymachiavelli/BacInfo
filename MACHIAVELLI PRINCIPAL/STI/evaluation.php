<?php

mysql_connect("localhost" , "root" , "") or die ("Error connecting ! ") ;
mysql_select_db("SWNUM") or die ("error selecting db ! ") ;

$id = $_POST["permis"] ; 
$auth = "SELECT * FROM  testeur WHERE numPermis = '$id'" ;
$check = mysql_query($auth) ;

$model = $_POST["modele"] ;
$sec = $_POST["sec"] ;
$cond = $_POST["cond"] ;
$conf = $_POST["conf"] ;

if (mysql_num_rows($check) > 0 ) {
    $check2= "SELECT * FROM evaluation WHERE numPermis = '$id' AND "
}
else{
    die("USER is not found ! ") ;

}


?>