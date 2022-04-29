<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <style>

        table , th , td{
            border:1px solid #000;
            border-collapse:collapse;

        }
        table{
            margin:auto;
            width:90%;
        }
        th,td{
            padding:10px;
        }
    </style>
  </head>
  <body>
<?php
//set the connection 

mysql_connect("localhost","root","") or die("could not connect to the server");
mysql_select_db("BDAlaaBarkag1") or die("could not connect to the database");

$id = $_POST['id'];
//check the id 
$checkEx = "SELECT id_musicien FROM musicien WHERE id_musicien='$id'";
$exiRes = mysql_query($checkEx);

if (mysql_num_rows($exiRes) == 0)
{
    $name = $_POST['name'];
    $age = $_POST['age'];
    $lname = $_POST['lname'];
    $ins = $_POST['instrument'];
    $req = "INSERT INTO musicien VALUES ('$id','$name','$lname','$age','$ins')";
    $res = mysql_query($req);
    
    if($res) {
        echo "Done saving the datas" ;
    }
    else {
        echo mysql_error();
    }
}
else
{
    echo "id already exist";
}


echo "<hr/><br/>";
?>

<h1>musiciens avec age >= 30</h1>
<table>
    <tr>
        <th>ID</th>
        <th>Nom</th>
        <th>Prenom</th>
        <th>Age</th>
        <th>Instrument</th>
    </tr>
    <?php
        $get = "SELECT * FROM musicien WHERE age >= 30";
        $getRes = mysql_query($get);
        while($row = mysql_fetch_array($getRes)) {?>
        <tr>
            <td><?php echo $row['id_musicien'] ?></td>
            <td><?php echo $row['nom'] ?></td>
            <td><?php echo $row['prenom'] ?></td>
            <td><?php echo $row['age'] ?></td>
            <td><?php echo $row['instrument'] ?></td>
        </tr>
        
    
    <?php } ?>
<table>

</body>
</html>