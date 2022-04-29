<?php
if(isset($_POST['id'])){
    mysql_connect("localhost","root","") or die("could not connect to the server");
    mysql_select_db("BDAlaaBarkag1") or die("could not connect to the database");
$id = $_POST['id'];


$req = "DELETE FROM musicien WHERE id_musicien = '$id'";

$res = mysql_query($req);

if($res) {
    echo "Done deleting the datas" ;
}
else {
    echo mysql_error();
}

}
else {
    echo "invalid datas" ;
}

?>