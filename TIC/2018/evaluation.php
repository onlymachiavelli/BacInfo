<?php
mysql_connect("localhost" , "root" , "");
mysql_select_db("bac2018");

$hotel= $_POST['hotel'];
$date = date("Y-m-d");
$query = "SELECT * FROM evaluation WHERE IdHotel = $hotel AND DateEval = '$date'";
$result = mysql_query($query);
if (mysql_num_rows($result) != 0) {
    die ("cet hotel est deja evaluee ! ") ;
}

else {
    $acc = $_POST['acc'];
    $res = $_POST['res'];
    $extra = intval($_POST['pc']) + intval($_POST['pp']) + intval($_POST['cw']) ;
    $req = "INSERT INTO evaluation values ('$date' , $hotel , $acc , $res , $extra)";
    $res = mysql_query($req);
    if ($res) {
        echo "evaluation reussie";
    }
    else {
        echo "evaluation echouee";
    }
}

?>