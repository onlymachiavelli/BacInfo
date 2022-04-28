<?php

mysql_connect("localhost","root","");

mysql_select_db("BW69420");


$check = "select * from client where tel='".$_POST['tel']."'";
if(mysql_num_rows(mysql_query($check))==0) {
    $req = "INSERT INTO client VALUES('".$_POST['tel']."','".$_POST['name']."','".$_POST['lname']."','".$_POST['adress']."','".$_POST['password']."')";   
    $res = mysql_query($req);
    if($res) {
        echo "Done saving datas" ;
    }
    else {
        echo "Cannot save the datas! perhaps the phone is already exist <br/>".mysql_error() ;
    }
}




else{ 
    echo "you can't save the datas";

}

?>