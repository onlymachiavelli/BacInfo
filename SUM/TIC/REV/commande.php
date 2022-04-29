<?php
mysql_connect("localhost","root","");
mysql_select_db("BW69420");
$type = $_POST["mySelect"] ;
$qte = $_POST['qte'];
$tel = $_POST["tel"] ;
$pass = $_POST["pass"] ;
$authReq = "select * from client where tel='$tel' and motpass='$pass'" ;
$isAuthed =mysql_query($authReq);
$date = date("Y-m-d H:i:s"); 
if (mysql_num_rows($isAuthed) > 0) {
    $req = "INSERT INTO commande VALUES ('$type','$tel' ,'$date', '$qte')";
    $res = mysql_query($req);
    if ($res) {
        echo "done ! " ;
    }
    else {
        echo "error saving the datas ! " .mysql_error();
    }
    
} 
else {
    echo "cannot do that because the user is not found ! " ;
}

?>