
<?php


mysql_connect("localhost", "root" , "" ) or die("Error connecting ");
mysql_select_db("2020") or die("Error  connecting ");

$req ="SELECT * FROM PIZZA " ;
$res= mysql_query($req) ;




?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All the datas ! </title>
    <style>
        table , td , th{
            border:1px solid #ff0000;
            border-collapse:collapse;
            padding:10px;
        }
        table{
            width:100%;
        }
    </style>
</head>
<body>
    

        <table>
            <tr>
            <th>Id Pizza</th>
            <th>Nom Pizza</th>
            <th>Details</th>
            <th>Prix Pizza</th>
            </tr>
            <?php
            while ($row = mysql_fetch_row($res)) {
            ?>  
            <tr>
                <td>
                    <?php  echo $row[0] ;?>
                </td>
                <td>
                    <?php  echo $row[1] ;?>
                </td>
                <td>
                    <?php  echo $row[2] ;?>
                </td>
                <td>
                    <?php  echo $row[3]; ?>
                </td>
            </tr>


            <?php }?>
        </table>
</body>
</html>