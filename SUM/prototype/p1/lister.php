<?php

//connect !  
mysql_connect("localhost", "root" , "") or die(mysql_error()."<br/>") ;
mysql_select_db("location") or die(mysql_error()."<br/>") ;



$req = "select * from voiture where disponible =N";
$res = mysql_query($req);


?>