<?php


function connectDB () {
    mysql_connect("localhost", "root", "") or die(mysql_error());
    mysql_select_db("piggietalk") or die(mysql_error());
}

function sendReq ($request, $get) {
    $res = mysql_query($request) or die(mysql_error());
    return $get ? mysql_affected_rows($res) : mysql_num_rows($res);
}     
?>