<?php
session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');


else {
$hostname = "localhost";
$username = "root";
$password = "";
$connection = new mysqli($hostname, $username, $password, "eleve");


if ($connection){
    
    $target_dir = "assets/uploads/";
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

    move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);
    $upload = "UPDATE users SET image = ('".$target_file."')  WHERE cin ='".$_SESSION['user']."'";
    echo $upload;
    if ($connection -> query($upload)){
        header("Location: profile.php");
    }
    else {
        die (mysqli_error($connection));
    }
}
else {
    print ("OH NO !");
}
}
?> 