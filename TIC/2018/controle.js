function Id(id) {
  return document.getElementById(id);
}

function Name(namme) {
  return document.getElementsByName(namme);
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
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
  return true;
}

function setCap() {
  Id("captcha").value = genCaptcha();
}

setCap();
