<?php
session_start();
if (!isset($_SESSION['user']) && !isset($_SESSION['pass'])) header('Location: ../login/login.php');

else {
    //
}
?>