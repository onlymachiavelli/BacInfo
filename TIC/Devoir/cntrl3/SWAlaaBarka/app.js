function Name(namme) {
  return document.getElementsByName(namme);
}

function Id(id) {
  return document.getElementById(id).value;
}

function verif() {
  var err = "";

  if (Id("id").length != 5 || Id("id")[0] != "M") {
    err += "Invalid Id \n";
  }
  if (Id("name").length > 10 || Id("name") == "") {
    err += "invalid name \n";
  }
  if (Id("lname").length > 10 || Id("lname") == "") {
    err += "invalid last name \n";
  }

  if (Number(Id("age")) < 5 || Number(Id("age")) > 99 || Id("age") == "") {
    err += "Invalid Age \n";
  }

  if (Name("instrument")[0].selectedIndex == 0) {
    err += "Select Instrument \n";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}

function del() {
  if (Name("id")[0].selectedIndex == 0) {
    alert("Select Instrument ");
    return false;
  }
  return true;
}
