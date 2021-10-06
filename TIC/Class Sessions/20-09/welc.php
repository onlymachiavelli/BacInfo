<?php

    $hostname = "localhost";
    $username = "root";
    $password = "";
    $connection = new mysqli($hostname, $username, $password, "eleve");
    function startsWith($string, $ele){
        for ($i =0;$i<count($ele);$i++) if( $string[$i] != $ele[$i]) return FALSE;
        return TRUE;
    }
    if($connection){
        $classes = [
            1 => 0,
            2=>0,
            3=>0,
            4=>0
        ];
        $action = "SELECT * FROM users";
        $res = $connection -> query($action);
    
        while ($row = $res -> fetch_assoc()){
            if(startsWith(strtolower($row['class']), "1ere")) $classes[1]++;
            else if(startsWith(strtolower($row['class']), "2eme")) $classes[2]++;
            else if(startsWith(strtolower($row['class']), "3eme")) $classes[3]++;
            else $classes[4]++;
    
        }
    }
    else {
        die ("error connecting to daya nase ");
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
                Nombre
            </td>
        </tr>
        <tr>
            <td>1Ere</td>
            <td>
                <?php
                    echo($classes[1]);
                ?>
            </td>
        </tr>

        <tr>
            <td>2Eme</td>
            <td>
                <?php
                    echo($classes[2]);
                ?>
            </td>
        </tr>

        <tr>
            <td>3Eme</td>
            <td>
                <?php
                    echo($classes[3]);
                ?>
            </td>
        </tr>

        <tr>
            <td>4Eme</td>
            <td>
                <?php
                    echo($classes[4]);
                ?>
            </td>
        </tr>
    </table>
    </div>
    <script src="./app.js"></script>
</body> 
</html>