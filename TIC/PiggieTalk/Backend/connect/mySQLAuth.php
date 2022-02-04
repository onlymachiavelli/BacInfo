<?php

function makeAuth($hostname, $username, $password, $dbName) {
    try{
        $authSql = new mysqli($hostname, $username, $password);
        return array([TRUE , $authSql]);
    }
    catch(e){
        return array([FALSE, e]);
    }
}


?>