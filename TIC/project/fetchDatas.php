<?php
//connecting

    mysql_connect($localhost,$username,$password) or die("Error connecting to phpMyadmin");
    mysql_select_db("formation") or die("Error selecting the database") ;




?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Getting all the datas !</title>
        
    </head>
    <body>
        <h1>All the dayas ! </h1>

        <br/>

        <table>
            <tr>
            <th>ID</th>
            <th>Nom</th>
            <th>Prenom</th>
            <th>Genre</th>
            <th>Email</th>
            <th>Bac</th>
            </tr>


        </table>
    </body>
</html>