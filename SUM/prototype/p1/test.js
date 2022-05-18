function Id(id) {
  return document.getElementById(id);
}

function Name(namme) {
  return document.getElementsByName(namme);
}

function isAlpha(myString) {
  for (var i = 0; i < myString.length; i++) {
    if (
      myString.charAt(i).toLowerCase() < "a" ||
      myString.charAt(i).toLowerCase() > "z"
    ) {
      return false;
    }
  }
  return true;
}

function test1() {
  var err = "";
  if (Id("ncin").value.length != 8 || isNaN(Id("ncin"))) {
    err += "NCIN field is invalid ! \n";
  }
  if (Id("nom").value.length < 3 || !isAlpha(Id("nom").value)) {
    err += "invalid name \n";
  }

  if (Id("prenom").value.length < 3 || !isAlpha(Id("prenom").value)) {
    err += "invalid last name \n";
  }

  var notallowedNumbers = new Array(0, 1, 6);
  var phone = true;
  for (var i = 0; i < 3; i++) {
    if (notallowedNumbers[i] === Number(Id("tel").value.charAt(0))) {
      phone = false;
    }
  }
  if (!phone || Id("tel").value.length !== 8 || isNaN(Id("tel").value)) {
    err += "Invalid phone ! \n";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}
