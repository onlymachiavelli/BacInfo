<?php


if (isset($_POST["station"]) && isset($_POST["saison"]) && isset($_POST["year"]) && isset($_POST["temp"]) && isset($_POST["pluie"])){


    mysql_connect("localhost", "root",  "") or die(mysql_error());
    mysql_select_db("bac2021")or die(mysql_error()) ;
    $checkReq = "select * from mesure where idstation='".$_POST["station"]."' and saison='".$_POST["saison"]."' and annee='".$_POST["year"]."'";

    $checkRes = mysql_query($checkReq);
    if (!$checkRes){
        //send datas

        echo "hello ";


        
    }
    else {
        echo "Mesures est deja enregistrees";
    }
}
else {
    echo "Error getting datas" ;
}


?>