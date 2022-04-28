function Id(id) {
  return document.getElementById(id).value;
}

function Name(namme) {
  return document.getElementsByName(namme);
}
function alpha(ch) {
  for (var i = 0; i < ch.length; i++) {
    if (ch[i].toUpperCase() < "A" || ch[i].toUpperCase() > "Z") {
      return false;
    }
  }
  return true;
}

function verif1() {
  var err = "";
  //our code !
  if (Id("name").length < 3 || !alpha(Id("name"))) {
    err += "Invalid Name ! \n";
  }
  if (Id("lname").length < 3 || !alpha(Id("lname"))) {
    err += "Invalid Last Name ! \n";
  }
  if (Number(Id("tel")[0]) < 2 || Id("tel").length != 8) {
    err += "Invalid phone number \n";
  }
  if (Id("adress").length < 10) {
    err += "Invalid Adress \n";
  }
  if (
    Id("password").indexOf(" ") != -1 ||
    Id("password") != Id("pass2") ||
    Id("password").length != 6
  ) {
    err += "Invalid password";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}
