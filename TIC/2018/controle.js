function Id(id) {
  return document.getElementById(id);
}

function Name(namme) {
  return document.getElementsByName(namme);
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}
function genCaptcha() {
  var cap = "";
  var k;
  for (var i = 0; i < 10; i++) {
    k = random(0, 26);
    if (k % 2 == 0) {
      cap += String.fromCharCode(k + 65);
    } else {
      cap += String.fromCharCode(k + 97);
    }
  }
  return cap;
}

function verifyCap(cap, res) {
  var capitals = 0;
  for (var i = 0; i <= cap.length; i++) {
    if (cap[i] >= "A" && cap[i] <= "Z") {
      capitals++;
    }
  }
  alert(capitals);
  return Number(res) === capitals;
}

function setCap() {
  Id("captcha").value = genCaptcha();
}

function numeric(ch) {
  for (var i = 0; i < ch.length; i++) {
    if (ch[i] < "0" || ch[i] > "9") {
      return false;
    }
  }
  return true;
}
function verif() {
  var err = "";
  if (Id("hotel").selectedIndex === 0) {
    err += "you should select a hotel \n ";
  }
  if (
    !Name("acc")[0].checked &&
    !Name("acc")[1].checked &&
    !Name("acc")[2].checked
  ) {
    err += "You should select a welcome type \n";
  }

  if (
    !Name("res")[0].checked &&
    !Name("res")[1].checked &&
    !Name("res")[2].checked
  ) {
    err += "You should select a reservation type \n";
  }
  if (numeric(Id("rep").value)) {
    if (!verifyCap(Id("captcha").value, Id("rep").value)) {
      err += "You should enter the correct number of capital letters \n";
    }
  } else {
    err += "You should enter a number \n";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
}

setCap();
