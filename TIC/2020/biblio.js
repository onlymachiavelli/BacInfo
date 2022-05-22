function Id(id) {
  return document.getElementById(id);
}

function Name(namme) {
  return document.getElementsByName(namme);
}

function isAlpha(ch) {
  for (var i = 0; i < ch.length; i++) {
    if (ch[i].toLowerCase() < "a" || ch[i].toLowerCase() > "z") {
      return false;
    }
  }

  return true;
}

function isNumber(ch) {
  for (var i = 0; i < ch.length; i++) {
    if (ch[i] > "9" || ch[i] < "0") {
      return false;
    }
  }
  return true;
}

function verif1() {
  var err = "";
  if (Id("nom").value.length < 3 || !isAlpha(Id("nom").value)) {
    err += "nom est  invaide ! \n";
  }
  if (Id("prenom").value.length < 3 || !isAlpha(Id("prenom").value)) {
    err += "prenom est  invaide ! \n";
  }
  if (!isNumber(Id("tel").value) || Id("tel").value.length !== 8) {
    err += "tel est invalide ! \n";
  } else {
    if (Number(ch[0]) <= 1) {
      err += "tel est invalide !  \n";
    }
  }

  if (Id("adresse").value.length < 10) {
    err += "adresse est invalide  ! \n ";
  }
  if (Id("pass").value.length != 6 || Id("pass").value.indexOf(" ") !== -1) {
    err += "mot de passe est invalide !  \n";
  }
  if (Id("pass2").value !== Id("pass").value || Id("pass").value.length === 0) {
    err += "Les mot de passe non compatible ! \n";
  }
  if (err.length > 0) {
    alert(err);
    return false;
  }
}
