<?php

    //datas is typed associated array 
    function postData($datas, $tableName,$path) {
        $req = "" ;
        $cols = "" ;
        $vals = "" ;
        foreach ($datas as $key => $value) {
            $cols .= $key . "," ;
            $vals .= "'" . $value . "'," ;
        }
        $req = "INSERT INTO $tableName ($cols) VALUES ($vals)" ;
        mysql_query($req) ;
        header("Location: $path");
    }
?>