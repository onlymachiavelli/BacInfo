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
function verif1() {
  var err = "";
  if (Id("nom").value.length < 3 || !isAlpha(Id("nom").value)) {
    if (err.length > 0) {
      alert(err);
      return false;
    }
  }
}
