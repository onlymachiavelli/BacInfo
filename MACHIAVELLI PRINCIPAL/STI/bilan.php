<?php

mysql_connect("localhost" , "root" , "") or die ("Error connecting ! ") ;
mysql_select_db("SWNUM") or die ("error selecting db ! ") ;


$req = "SELECT DISTINCT a.libelle, AVG( b.securite ) , AVG( b.conduite ) , AVG( b.confort ) , COUNT( b.idModele )
FROM evaluation b, modelevoiture a
WHERE a.idModele = b.idModele
GROUP BY a.idModele" ;


$res =mysql_query($req) ;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bilan</title>
    <style>
        table, td ,th {
            border:1px solid #000 ;
            border-collapse:collapse;
            padding:10px;
        }
        table{
            padding:10px;
            width:100%;
        }
    </style>
</head>
<body>
    

<div>
    <table>
        <tr>
        <th>Modele</th>
        <th>Securite</th>
        <th>Conduite</th>
        <th>Confort</th>
        <th>Nbr tests</th>
        </tr>
        <?php while ($row = mysql_fetch_array($res)) {?>
            <tr>
                <td><?php echo $row[0]; ?></td>
                <td><?php echo $row[1]; ?></td>
                <td><?php echo $row[2]; ?></td>
                <td><?php echo $row[3]; ?></td>
                <td><?php echo $row[4]; ?></td>

            </tr>
            
        <?php }?>
    </table>

</div>
</body>
</html>