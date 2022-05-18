<?php

if (isset($_POST["serie"]) && isset($_POST["enr"])) {
    //connect !  
    mysql_connect("localhost", "root" , "") or die(mysql_error()."<br/>") ;
    mysql_select_db("location") or die(mysql_error()."<br/>") ;

    $fullserie = $_POST["serie"]."TU".$_POST["enr"] ;
    //check car 
    $car = "select * from voiture where Imat='$fullserie'" ;
    $carRes = mysql_query($car) ;
    if (mysql_num_rows($carRes) ==0) {
        die ("car doesn't exist ! ") ;
    }
    else {
        $row = mysql_fetch_array($carRes) ;
        if ($row["Disponible"] == "D"){
            die ("car is dispo @! ");
        }
        else {
            $req = "update voiture set Disponible='N' where Imat='$fullserie'" ;
            $res = mysql_query($res) ;
            if ($res) {
                print("Done saving the datas ! ") ;
            }
            else {
                die (mysql_error());
            }
        }
    }
}

?>