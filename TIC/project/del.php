<?php
    if(isset($_POST['option']) && $_POST['option'] != "0" ){

        mysql_connect("localhost","root","") or die("Error connecting to phpMyadmin");
        mysql_select_db("formation") or die("Error selecting the database") ;
        
        
        $req = "DELETE FROM condidat WHERE id='".$_POST['option']."'"; 
        $res = mysql_query($req) ;
        if ($res) {
            echo "Done deleting datas ! "; 
        }
        else {
            echo "Error deleting the data ! perhpas there's an error !";
            echo "<br/> " . mysql_error() ;
        }
        echo "<br/> <a href='fetchDatas.php'>Goo back</a>";
    }
    else {
        echo "Error getting choice" ;
    }
?>