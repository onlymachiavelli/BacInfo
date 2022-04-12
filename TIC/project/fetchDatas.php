<?php

    mysql_connect("localhost","root","") or die("Error connecting to phpMyadmin");
    mysql_select_db("formation") or die("Error selecting the database") ;

    $req = "SELECT * FROM condidat";
    $res = mysql_query($req) ;

?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Getting all the datas !</title>
        <style>
            table{width:100%;}
            table, th, tr, td {
                border:1px solid black;
                border-collapse: collapse;
            }
            td, th{
                padding:7px;
            }
        </style>
    </head>
    <body>
        <h1>All the datas ! </h1>
        <a href="./index.html">Do you want to add a data ? </a>
        <br/>
        <a href="./update.html">Update email ? </a>


        <br/><br/>

        <table>
            <tr>
                <th>ID</th>
                <th>Nom</th>
                <th>Prenom</th>
                <th>Genre</th>
                <th>Email</th>
                <th>Bac</th>
                <th>Delete</th>
            </tr>
            <?php while ($row = mysql_fetch_array($res)) {?>
            <tr>
                <td><?php echo $row['id'] ?></td>
                <td><?php echo $row['nom'] ?></td>
                <td><?php echo $row['prenom'] ?></td>
                <td><?php echo $row['genre'] ?></td>
                <td><?php echo $row['email'] ?></td>
                <td><?php echo $row['bac'] ?></td>
                <td> 
                    <form method="POST" action="./delete.php">
                        <input type="hidden" name="id" value="<?php echo $row['id'] ?>"/>
                        <input type="submit" name="delete" value="Delete"/>
                    </form>
                </td>
            </tr>
            <?php } ?>

        </table>
    </body>
</html>