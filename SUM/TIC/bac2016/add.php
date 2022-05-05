<?php

//connect  to the SERVER 
mysql_connect("localhost" , "root" , "") or die("Error connecting to the server") ;
mysql_select_db("bac2016") or die("Error connecting to the db") ;

$date = $_POST['year']."-".$_POST['month']."-".$_POST['day'] ;

$peace = $_POST['peace'] ;
$salle = $_POST['salle'] ;
$checkSalle = "SELECT Idsalle from spectacle WHERE Idsalle=$salle AND DateSpectacle=$date";
$sl = mysql_query($checkSalle);


if(!$sl) {
    //ekhdem ! 

    $checkPeace = "SELECT Idpiece FROM spectacle WHERE Idpiece=$peace";
    $pc = mysql_query($checkPeace) ;
    if (mysql_num_rows($pc) == 0) {
        
        $req = "INSERT INTO spectacle VALUES('$peace', '$date', '$salle')";
        $res = mysql_query($req) ;
        
        if ($res) {
            echo "done saving the datas" ;
        }
        else {
            echo "error saving the datas ! <br/> ".mysql_error() ;
        }
    }



    else {
        echo "Piece deja programmee" ; 
    }
}
else{
    //err
    echo "salle non disponible" ; 
}

?>