<?php
//connect 
$localhost = "localhost";
$username = "root";
$password = "";
mysql_connect($localhost,$username,$password);

$fullname = $_POST['name'];
$name = "";
$lname = "" ;
for ($i=0;$i<strlen($fullname);$i++){
    if ($fullname[$i] == " "){
        $name = substr($fullname,0,$i);
        $lname = substr($fullname,$i+1,strlen($fullname));
        break;
    }
}


$reqDatas = array(
    "name" =>$name,
    "lname" =>$lname,
    "sex" =>$_POST['sex'],
    "email" =>$_POST['email'],
    "bac" =>$_POST['nc'],
);

foreach($reqDatas as $key => $value) {
    echo "$value <br/>" ;
}
//select database
mysql_select_db("formation");

$req = "INSERT INTO CONDIDAT (nom,prenom,genre,email,bac) VALUES ('".$reqDatas['name']."','".$reqDatas['lname']."','".$reqDatas['sex']."','".$reqDatas['email']."','".$reqDatas['bac']."')";
mysql_query($req);
header('Location: index.html');
?>