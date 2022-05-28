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
    $check2= "SELECT * FROM evaluation WHERE numPermis = '$id' AND idModele=$model" ;
    $checkres = mysql_query($check2);
    if (mysql_num_rows($checkres) >0) {
        die ("already rated ! ") ;
    }
    else {
        $date = date("Y-m-d h:i:s") ;
        $req = "INSERT INTO evaluation VALUES('$id', $model,'$date', $sec, $cond, $conf)";
        $res = mysql_query($req) ;
        if ($res){
            print("Done saving the datas ! ") ;

        }
        else {
            die (mysql_error() );
        }
    }
}
else{
    die("USER is not found ! ") ;

}

mysql_close();


?>