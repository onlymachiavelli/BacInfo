<?php

session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');


$hostname = "localhost";
$username  ="root";
$password = "";
$connection = new mysqli($hostname, $username, $password, "eleve");

function getTarget ($target){
    global $connection;
    $date = "SELECT * FROM users WHERE cin = ".$_SESSION['user'];
    $res = mysqli_query($connection, $date);
    while ($row = $res -> fetch_assoc()){
        return ($row[$target]);
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo "Welcome ". getTarget("fullname")  ?></title>
    <link  rel="stylesheet" href="main.css" />
    <link rel="stylesheet" href="./../global.css" />
    <link rel="stylesheet" href="./../assets/font-awesome/css/font-awesome.css" />
</head>
<body>
    <header>
        <nav class="navbar"> 
            <div class="logo">
                <a href="">
                    <img src="./../assets/school.png" />
                </a>
            </div>
            <nav class="nav">
                <a href="">Acceuil</a>
                <a href="">Mes Informations</a>
                <a href="">Ma Classe</a>
                <a href="">Parametres</a>
            </nav>
            <div class="logoutbtn">
                <form action="logout.php">
                    <button type="submit">LogOut</button>
                </form>
            </div>
        </nav>
    </header>
    <br/><br/>
    <main class="card_container">
        <div class="card">
            <div class="img">
                <img src="./IMG_20210919_011817_286.png" alt="profile Picture"  />
                <p class="date">
                    
                <?php
                    echo "Cree Le ".getTarget("creationdate");
                ?>
                </p>
            </div>
            <div class="infos">
                <br/>
                <table class="data">
                    <tr>
                        <th>Nom :</th>
                        <th><?php echo getTarget("fullname");?></th>

                    </tr>
                    <tr>
                        <th>Date de naissance</th>
                        <th><?php echo getTarget("date");?></th>

                    </tr>
                    <tr>
                        <th>Classe</th>
                        <th>
                            <?php
                             $classes = "SELECT * FROM classes";
                             $ress = mysqli_query($connection, $classes);
                             $options = array();
                             while($row = $ress -> fetch_assoc()){
                                 array_push($options, $row['class']);
                             }
                                if(getTarget("class") == NULL) {
                                    echo ("
                                    <form method='POST' action='class.php' >
                                    
                                    <select name='userclass'>
                                        <option value =NULL>Selectionner Votre Classe</option>
                                    ");
                                    for ($i=0;$i<count($options);$i++){
                                        echo "<option vaue='".
                                        $options[$i]
                                        ."'>".$options[$i]."</option>";
                                    }
                                       
                                       echo ("
                                    </select>
                                    <button type='submit' class='sendbtn' >Send</button>
                                        
                                    </form>
                                ");
                                }
                                else echo getTarget("class");

                                
                            ?>
                        </th>

                    </tr>
                    <tr>
                        <th>CIN Tunis</th>
                        <th>
                            <?php echo getTarget("cin");?>
                        </th>

                    </tr>
                </table>

            </div>
        </div>
    </main>
</body>
</html> 