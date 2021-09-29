<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <link rel="stylesheet" href="./style.css" />
    <link rel="stylesheet" href="./../assets/font-awesome/css/font-awesome.css" />
    <link rel="stylesheet" href="./../global.css" />
</head>

<body>
    <main class="signup">
        <div class="logo">
            <a href="./../index.html">
                <img src="./../assets/school.png" />
            </a>
        </div>
        <br />
        <section class="form_section"> 
            <br /><br />
            <form action="create.php" method="POST">
                <div class="txtinp">
                    <i class="fa fa-user-circle" aria-hidden="true"></i>
                    <input type="text" name="lname" placeholder="Votre Nom" required />
                </div>
                <div class="txtinp">
                    <i class="fa fa-id-card" aria-hidden="true"></i>
                    <input type="text" name="cin" placeholder="VOTRE CIN" required />
                </div>
                <div class="txtinp">
                    <i class="fa fa-calendar" aria-hidden="true"></i>
                    <input type="date" name="date" required />
                </div>


                <div class="txtinp passtxt">
                    <i class="fa fa-lock" aria-hidden="true"></i>
                    <input type="password" name="pass" placeholder="Le Mot De Passe" class="pass" required/>
                    <button type="button" class="eye" onclick="setInpType('pass', 'eye')">
                        <i class="fa fa-eye" aria-hidden="true"></i>
                    </button>
                </div>
                <br/>
                <div class="picker_container">
                    <div class="picker">
                        <i class="fa fa-male" aria-hidden="true"></i>
                        &nbsp;
                        <b>Male</b>
                        <input type="radio" name="gender" value = "male" />
                    </div>
                    
                    <div class="picker">
                        <i class="fa fa-female" aria-hidden="true"></i>
                        &nbsp;
                        <b>Female</b>
                        <input type="radio" name="gender" value = "female" />
                    </div>
                </div>


                <div class="txtinp">
                    <i class="fa fa-envelope" aria-hidden="true"></i>
                    <input type="email" name="email" required  placeholder="Email"/>
                </div>

                <div class="txtinp">
                    <i class="fa fa-phone" aria-hidden="true"></i>
                    <input type="tel" name="phone" required  placeholder="Phone"/>
                </div>
                <textarea name="adress" placeholder="Votre Adresse" class="adress" ></textarea>
                <p id="tit">Center D'interets</p>
                <div class="picker_container p">
                    <div class="picker">
                        <i class="fa fa-music" aria-hidden="true"></i>
                        &nbsp;
                        <b>Music</b>
                        <input type="checkbox" name="music" value = "music" />
                    </div>



                    <div class="picker">
                        <i class="fa fa-globe" aria-hidden="true"></i>
                        &nbsp;
                        <b>Internet</b>
                        <input type="checkbox" name="internet" value = "internet" />
                    </div>


                    <div class="picker">
                        <i class="fa fa-camera" aria-hidden="true"></i>
                        &nbsp;
                        <b>Phgraph</b>
                        <input type="checkbox" name="photograph" value = "photo" />
                    </div>

                </div>
                <button type="submit" class="createbtn">
                    Create
                </button>
            </form>
            <a href="./../Login/login.php">VousAvez Un Compte ? </a>
        </section>
    </main>
    <script src="./../app.js"></script>
</body>

</html>