<?php

//connect !  
mysql_connect("localhost", "root" , "") or die(mysql_error()."<br/>") ;
mysql_select_db("location") or die(mysql_error()."<br/>") ;



$req = "select * from voiture where Disponible='N'";
$res = mysql_query($req);


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <?php
    
        if (mysql_num_rows($res) ==0) {
            echo "<h1>No datas ! </h1>" ;
        }
        else {
            while ($row=mysql_fetch_row($res)){
                ?>
            <table>
                <tr>
                <th>Matricule Voiture</th>
                <th>Modele  Voiture</th>
                <th>Prix de location </th>
                </tr>

                <tr>
                <td><?php echo $row["Imat"] ;?></td>
                <td><?php echo $row["Model"] ;?></td>
                <td><?php echo $row["PrixLoc"] ;?></td>
                </tr>
            </table>

        <?php }}?>
    ?>
    
</body>
</html>