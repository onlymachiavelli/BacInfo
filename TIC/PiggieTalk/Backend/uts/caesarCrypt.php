<?php
    function Caesar($string, $shift, $crypt) {
        $newString = "";
        for ($i =0;$i<strlen($string);$i++){
            $asc = $crypt ? ord($string[$i]) + $shift : ord($string[$i]) - $shift;
            $newString .= chr($asc );
        }
        return ($newString);
    }
    echo Caesar("Khoor#Zruog$", 3, false);


?>