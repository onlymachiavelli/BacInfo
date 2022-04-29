<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <form action="./suppr.php" method="POST" onsubmit="return del()">
      <fieldset>
        <legend>Supprimer un musicien</legend>

        <label>Identifiant musicien : </label>
        <select name="id" id="id">
          <option>Selectionner un ID</option>
          <?php
          
          mysql_connect("localhost","root","") or die("could not connect to the server");
          mysql_select_db("BDAlaaBarkag1") or die("could not connect to the database");

          $req = "SELECT id_musicien FROM musicien";
          $res = mysql_query($req);
          if (mysql_num_rows($res) > 0)
          {
            while ($row = mysql_fetch_assoc($res))
            { ?>
              <option value="<?php echo $row['id_musicien'] ?>"> <?php echo $row['id_musicien'] ?></option>;
            <?php }} ?>
          
          
        </select>

        <button type="submit" >Supprimer</button>
      </fieldset>
    </form>
    <script src="app.js"></script>
  </body>
</html>
