function Id(id) {
  return document.getElementById(id);
}

function Name(namme) {
  return document.getElementsByName(namme);
}

function Test1() {
  var err = "";

  if (Name("station")[0].selectedIndex == 0) {
    err += "selectioner la station \n";
  }
  if (Name("saison")[0].selectedIndex == 0) {
    err += "Selectioner saison \n";
  }
  if (!Name("year")[0].checked && !Name("year")[1].checked) {
    err += "choisir l'annee \n";
  }
  if (
    Number(Name("temp")[0].value) < -5 ||
    Number(Name("temp")[0].value) > 50 ||
    Name("temp")[0].value == "" ||
    isNaN(Name("temp")[0].value)
  ) {
    err += "temperature invalide \n";
  }
  if (Number(Name("pluie")[0].value) < 0 || Name("pluie")[0].value == "") {
    err += "pluie option invalide";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}

function Test2() {
  var err = "";
  if (Name("station")[0].selectedIndex == 0) {
    err += "Selectionner une station \n";
  }
  if (!Name("clim")[0].checked && !Name("clim")[0].checked) {
    err += "Selectionnee unde donne climatique \n";
  }
  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}
