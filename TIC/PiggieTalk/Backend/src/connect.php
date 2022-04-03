<?php


function connectDB () {
    mysql_connect("localhost", "root", "") or die(mysql_error());
    mysql_select_db("piggietalk") or die(mysql_error());
}

function sendReq ($request) {
    mysql_query($request) or die(mysql_error());
}
?>