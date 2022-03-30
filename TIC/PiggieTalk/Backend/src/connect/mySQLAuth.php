<?php

function connect($username, $password, $dbName) {
    mysql_connect("localhost", $username, $password) ;
    mysql_select_db($dbName) ;
}
?>
