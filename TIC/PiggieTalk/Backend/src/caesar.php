<?php
function caesar($message, $shift, $code){
    $msg = "" ;
    $cof = $code ? 1 : -1 ;
    for ($i=0;$i<strlen($message);$i++){
        $msg .= chr(ord($message[$i]) +( $shift*$cof));
    }
    return $msg;
}


?>