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

    <style>
        table, td, th{
            border:1px solid #000;
            border-collapse:collapse; 
        }
        table{
            width:90%;
            
        }
        td, th{
            padding:10px;
        }
    </style>
</head>
<body>
<table>
<tr>
                <th>Matricule Voiture</th>
                <th>Modele  Voiture</th>
                <th>Prix de location </th>
                </tr>
    <?php
    
        
            while ($row=mysql_fetch_array($res)){
                ?>
            
                

                <tr>
                <td><?php echo $row["Imat"] ;?></td>
                <td><?php echo $row["Model"] ;?></td>
                <td><?php echo $row["PrixLoc"] ;?></td>
                </tr>
            

        <?php }?>
        </table>
    
    
</body>
</html>