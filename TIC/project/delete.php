<?php
if (isset($_POST['id'])){
    mysql_connect("localhost", "root" , "") or die ("Error connecting to phpMyadmin ");
    mysql_select_db("formation") or die ("Error selecting the database") ;

    $req = "DELETE FROM condidat WHERE id = ".$_POST['id']; 
    $res = mysql_query($req) ;
    if (mysql_affected_rows() >0 ) {
        echo "Done deleting datas ! "; 
    }
    else {
        echo "Error deleting the data ! perhpas there's an error !";
        echo "<br/> " . mysql_error() ;
    }
    echo "<br/> <a href='fetchDatas.php'>Goo back</a>";
}
else{
    echo "Error getting datas ! ";
}

?>