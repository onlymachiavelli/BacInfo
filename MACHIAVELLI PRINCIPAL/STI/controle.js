const Id = (id) => document.getElementById(id)
const Name = (namme) => document.getElementsByName(namme)

const isAlpha = (ch) => {
  for (let i = 0; i < ch.length; i++) {
    if (ch[i].toUpperCase() > "Z" || ch[i].toUpperCase() < "A") {
      return false
    }
  }
  return true
}

const isNum = (ch) => {
  for (let i = 0; i < ch.length; i++) {
    if (ch[i] > "9" || ch[i] < "0") {
      return false
    }
  }
  return true
}
const verif1 = () => {
  let err = ""

  if (
    Id("permis").value.length !== 8 ||
    !isNum(Id("permis").value.substr(0, 2)) ||
    Id("permis").value[2] != "/" ||
    !isNum(Id("permis").value.substr(3, 5))
  ) {
    err += "invalid driver license \n"
  }
  if (
    Id("nom").value.length < 3 ||
    Id("nom").value.length > 20 ||
    !isAlpha(Id("nom").value)
  ) {
    err += "Invalid name ! \n"
  }

  if (
    Id("prenom").value.length < 3 ||
    Id("prenom").value.length > 20 ||
    !isAlpha(Id("prenom").value)
  ) {
    err += "Invalid last name  ! \n"
  }
  if (!Name("sex")[0].checked && !Name("sex")[1].checked) {
    err += "Select a sex ! \n"
  }

  if (err.length > 0) {
    alert(err)
    return false
  }
  return true
}

const verif2 = () => {
  let err = ""

  if (
    Id("permis").value.length !== 8 ||
    !isNum(Id("permis").value.substr(0, 2)) ||
    Id("permis").value[2] != "/" ||
    !isNum(Id("permis").value.substr(3, 5))
  ) {
    err += "invalid driver license \n"
  }

  if (Id("modele").selectedIndex === 0) {
    err += "you should select model \n"
  }
  if (isNum(Id("sec").value)) {
    if (Number(Id("sec").value) > 5 || Number(Id("sec").value) < 1) {
      err += " security number is out of interval ! \n"
    }
  } else {
    err += "invalid security number ! \n"
  }

  if (isNum(Id("cond").value)) {
    if (Number(Id("cond").value) > 5 || Number(Id("cond").value) < 1) {
      err += " ride number is out of interval ! \n"
    }
  } else {
    err += "invalid ride number ! \n"
  }
  if (isNum(Id("conf").value)) {
    if (Number(Id("conf").value) > 5 || Number(Id("conf").value) < 1) {
      err += " comfort number is out of interval ! \n"
    }
  } else {
    err += "invalid comfort number ! \n"
  }
  if (!Id("robot").checked) {
    err += "proof that you're not a robot ! \n"
  }

  if (err.length > 0) {
    alert(err)
    return false
  }
  return true
}
