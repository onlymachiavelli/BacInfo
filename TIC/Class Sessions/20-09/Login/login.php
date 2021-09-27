<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="./../global.css" />
    <link rel="stylesheet" href="./../Login/style.css" />
    <link rel="stylesheet" href="./../assets/font-awesome/css/font-awesome.css" />
</head>
<body>
    <main class="login_container">
        <div class="log_flex">
            <div class="welc_login">
                <div class="image-side">
                    <img src="./../assets/school.png" />
                </div>
                <p id="welc_desc">Bienvenue dans l’espace des eleves</p>
            </div>

            <div class="inp_areas">
                <p id="log_title">Espace Eleve</p>
                <form method="POST" action="auth.php"> 
                    <div class="txtinp">
                        <i class="fa fa-id-card" aria-hidden="true"></i>
                        <input type="text" name="cin" placeholder="VOTRE CIN" required />
                    </div>

                    <div class="txtinp passtxt">
                        <i class="fa fa-lock" aria-hidden="true"></i>
                        <input type="password" name="pass" placeholder="Le Mot De Passe" class="pass" required/>
                        <button type="button" class="eye" onclick="setInpType('pass', 'eye')">
                            <i class="fa fa-eye" aria-hidden="true"></i>
                        </button>
                    </div>

                    <button type="submit" class="login_btn">
                        Login
                    </button>
                </form>
                <a href="#" class="tocr">
                    Create One
                </a>
                <br/>
                <a href="./../signup/signup.html" id="forgot">Oublié votre mot de passe ?</a>
            </div>
        </div>
    </main>
    <script src="./../app.js"></script>
</body>
</html>

