<?php

    $hostname = "localhost";
    $username = "root";
    $password = "";
    $connection = new mysqli($hostname, $username, $password, "eleve");

    if($connection){
        print("Connected");

    }
    else {
        die ("error connecting to daya nase ");
    }

    $premiere  = 0;
    $deux = 0;
    $troi = 0;
    $bac = 0;
    function In($arr, $obj){
        for ($i=0;$i<size($arr);$i++){
            if ($obj == $arr[i]) return TRUE;
        }
        return FALSE;
    }
    $action = "SELECT * FROM users";
    $res = $connection -> query($action);
    while ($row = $res -> fetch_assoc()){
        switch ($row['class']){
            case "1ERE": 
                $premiere++;
                break;
            case ""
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet"  href="./global.css"/> 
</head>
<body>
    <div>
    <h1>
        Welcome User 
    </h1>
    <table>
        <tr>
            <th colspan="2">
                Total Classes !
            </th>
        </tr>
        <tr>
            <td>
                Classe : 
            </td>
            <td>
                4eme Science Informatique
            </td>
        </tr>
    </table>
    </div>
    <script src="./app.js"></script>
</body> 
</html>