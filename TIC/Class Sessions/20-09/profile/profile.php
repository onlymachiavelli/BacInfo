<?php

session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');


$hostname = "localhost";
$username  ="username";
$password = "password";
$connection = new mysqli($hostname, $username, $password, "eleve");
$isconnected = FALSE;
if ($connection) $isconnected = TRUE;
else $isconnected = FALSE; 
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link  rel="stylesheet" href="main.css" />
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
                    <button>LogOut</button>
                </form>
            </div>
        </nav>
    </header>
    <br/><br/>
    <main class="card_container">
        <div class="card">
            <div class="img">
                <img src="./IMG_20210919_011817_286.png" alt="profile Picture"  />
                <p class="date">Cree Le 21/12/1999</p>
            </div>
            <div class="infos">
                <br/>
                <table class="data">
                    <tr>
                        <th>Nom :</th>
                        <th>Barka Alaa</th>

                    </tr>
                    <tr>
                        <th>Date de naissance</th>
                        <th>04/07/2002</th>

                    </tr>
                    <tr>
                        <th>Classe</th>
                        <th>4eme Informatique</th>

                    </tr>
                    <tr>
                        <th>CIN Tunis</th>
                        <th>014896325</th>

                    </tr>
                </table>

            </div>
        </div>
    </main>
</body>
</html> 