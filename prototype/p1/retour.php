<?php

if (isset($_GET["serie"]) && isset($_GET["enr"])) {
    //connect !  
    mysql_connect("localhost", "root" , "") or die(mysql_error()."<br/>") ;
    mysql_select_db("location") or die(mysql_error()."<br/>") ;

    $fullserie = $_GET["serie"]."TU".$_GET["enr"] ;
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
            $cdate = date("y-m-d h-m-s") ;
            $req = "update voiture set Disponible='D' where Imat='$fullserie'" ;
            $res = mysql_query($req) ;
            if ($res) {
                $res2 = mysql_query("update louer set DateRet='$cdate' where Imat='$fullserie'");
                if ($res2) {
                    print("Finally ! ") ;
                }
                else {
                    die ("whaat ! ") ; 
                }
                
            }
            else {
                die (mysql_error());
            }
        }
    }
}

?>