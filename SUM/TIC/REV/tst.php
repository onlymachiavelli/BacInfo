<?php

$data = $_POST['num'];

mysql_connect("localhost"  , "root" , "" ) or die(mysql_error());
mysql_select_db("users" ) or die(mysql_error());

$check = "select phone from hitler where phone=".$data;
$resCheck = mysql_query($check) ;

if (mysql_num_rows($resCheck) == 0){
    echo "we ccan add the datas! " ;
}
 else  {
    echo "data already exists " ; 

 }

?>