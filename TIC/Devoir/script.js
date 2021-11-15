function Id(id) {
  return document.getElementById(id);
}
function Name(name) {
  return document.getElementsByName(name);
}

function isAlpha(myString) {
  if (myString.length === 0) return false;
  const alpha = "abcdefghijklmnopqrstuvwxyz";
  for (let i = 0; i < myString.length; i++) {
    if (myString[i] !== " ") {
      if (alpha.indexOf(myString[i].toLowerCase()) === -1) {
        return false;
      }
    }
  }
  return true;
}

function checkSex() {
  for (let i = 0; i < Name("sex").length; i++) {
    if (Name("sex")[i].checked) {
      return true;
    }
  }
  return false;
}

function Test() {
  error = ``;
  let finalCheck = true;
  mr = "";
  if (!checkSex()) {
    finalCheck = false;
    error += "you have to choose your genre ! \n";
  }

  if (!isAlpha(Id("name").value)) {
    finalCheck = false;
    error += "Wrong name please re type it \n";
  }
  if (Id("matr").value.length !== 4) {
    finalCheck = false;
    error += "Matricule is not 4 characters !! \n";
  }

  if (Name("sex")[0].checked) mr = "Mr";
  else mr = "Madame";

  if (finalCheck) {
    msg = "Vous etes bien ajouter " + mr + " " + Id("name").value;
    Id("myMsg").innerHTML = msg;
  } else {
    alert(error);
  }
}

function Reset() {
  for (let i = 0; i < Id("sex").length; i++) {
    Id("sex")[i].checked = false;
  }
  Id("name").value = "";
  Id("matr").value = "";
  Id("myMsg").innerHTML = "";
}
