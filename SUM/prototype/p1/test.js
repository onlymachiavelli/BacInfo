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

const Number = (myString) => {
  for (let i = 0; i < myString.length; i++) {
    if (myyString[i] < "0" || myString[i] > "9" || myString[0] != "-") {
      return false;
    }
  }
  return true;
};

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

function verif2() {
  var err = "";
  if (Id("serie").value.length !== 3 || isNaN(Id("serie").value)) {
    err += "Invalid serie Number ! \n";
  }
  if (!isNaN(Id("enr").value)) {
    if (Number(Id("enr").value) > 9999 || Number(Id("enr").value) < 1) {
      err += "Invalid ENRG \n";
    }
  } else {
    err += "Invalid enrg \n";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}
