<?php
    function getData($tableName, $cols, $where) {
        $req = "SELECT $cols FROM $tableName WHERE $where" ;
        $res = mysql_query($req) ;
        $data = mysql_fetch_assoc($res) ;
        return $data ;
    

    }
    function getAll($tableName) {
        $req = "SELECT * FROM $tableName" ;
        $res = mysql_query($req) ;
        $data = array() ;
        while ($row = mysql_fetch_assoc($res)) {
            array_push($data, $row) ;
        }
        return $data ;
    }
?>