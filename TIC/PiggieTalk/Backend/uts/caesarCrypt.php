<?php
    function caesar($string, $shift) {
        $newString = "";
        for ($i =0;$i<strlen($string);$i++){
            $asc = ord($string[$i]) + $shift;
            echo $asc . "<br/>";
            $newString .= chr($asc );
        }
        return ($newString);
    }
    function diCaesar ($string, $shift) {
        $newString = "";
        for ($i =0;$i<strlen($string);$i++){
            $asc = ord($string[$i]) - $shift;
            echo $asc . "<br/>";
            $newString .= chr($asc );
        }
        return ($newString);
    }

?>