<?php
//check the datas ! 


if (isset($_POST["ncin"]) && isset($_POST["nom"]) && isset($_POST["prenom"]) && isset($_POST["tel"])) {
    //connect !  
    mysql_connect("localhost", "root" , "") or die(mysql_error()."<br/>") ;
    mysql_select_db("location") or die(mysql_error()."<br/>") ;

    //check dubl !  
    $id = $_POST["ncin"];
    $dub = "select * from client where ncin='$id'";
    $dubRes = mysql_query($dub);
    if (mysql_num_rows($dubRes) >0) {
        die ("this user is already exists! ") ;
    }
    else {
        //saving the datas ! 
        $name = $_POST["nom"];
        $lname = $_POST["prenom"]; 
        $tel = $_POST["tel"] ;
        $req = "insert into client values ('$id','$name','$lname','$tel')";
        $res = mysql_query($req);
        if ($res) {
            print("Done saving the datas ! ") ; 

        }
        else {
            die (mysql_error());
        }
    }
}

else {
    print("Didn't get any data ! ") ;
}


?>