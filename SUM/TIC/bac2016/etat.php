<?php
mysql_connect("localhost" , "root" , "") or die("Error connecting to the server") ;
mysql_select_db("bac2016") or die("Error connecting to the db") ;


$req = "SELECT p.Titre, s.libelle , sp.DateSpectacle , sp.Idpiece ,sp.Idsalle , s.Idpiece, p.Idpiece, s.Idsalle FROM piece AS p, salle AS  s, spectacle AS  sp WHERE sp.Idpiece = p.Idpiece AND sp.Idsalle = s.Idsalle";
$res = mysql_query($req);


?>

