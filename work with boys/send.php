<?php
$servername = "localhost" ;
$username = "root" ;
$password = "" ; 

$dbnamme = "formation2";
mysql_connect($servername, $username, $password);
mysql_select_db($dbnamme);


$fullname = $_POST['name'];
$name = "";
$lname = "" ;

for ($i=0;$i<strlen($fullname);$i++){
    if ($_POST['name'][$i] == " " ){
        $name = substr($fullname, 0, $i);
        $lname = substr($fullname, $i+1, strlen($fullname));
        break;
    }
}

$req = "INSERT INTO `condidat` ( `nom`, `prenom`, `genre`, `email`, `bac`) VALUES ('".$name."', '".$lname."', '".$_POST['sex']."', '".$_POST['email']."', '".$_POST['nc']."')";

mysql_query($req);

header('Location: index.html');



?>