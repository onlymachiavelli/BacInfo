<?php
if(isset($_POST['email'])&& isset($_POST['id'])) {
    
    mysql_connect("localhost" , "root" , "") or die("Error connecting to phpMyadmin") ;
    mysql_select_db ("formation") or die ("Error selecting the database") ;


    $find = "SELECT * FROM condidat WHERE id = '".$_POST['id']."'";
    $findUser = mysql_query($find) ;
    if (mysql_num_rows($findUser) >0 ) {
        $req = "UPDATE condidat SET email = '".$_POST['email']."' WHERE id = '".$_POST['id']."'";
        $res = mysql_query($req) ;
        if ($res) {
            echo "success updating";
        } else {
            echo "error updating " . mysql_error() . "<br/>";
        }
    }
    else {
        echo "User's not found ! Can't update ! <br/>" ;
    }
    


}

else {
    echo "Error getting the datas ! ";  
}

echo "<br/><a href='./update.html'>Go back</a>";

?>