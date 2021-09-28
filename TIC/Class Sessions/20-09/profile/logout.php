<?php


session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');


//LOG OUT 
session_unset();
session_destroy();
header('Location: ../login/login.php');
?>