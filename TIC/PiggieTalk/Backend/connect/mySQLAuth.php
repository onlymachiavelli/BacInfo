<?php

function makeAuth($hostname, $username, $password, $dbName) {
    try{
        $authSql = new mysqli($hostname, $username, $password);
    }
    catch(e){
        return array([FALSE, e]);
    }
}


?>