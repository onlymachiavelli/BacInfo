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
const verif = () => {
  let err = ""

  if (
    Id("permis").value.length !== 8 ||
    !isNum(Id("permis").value.substr(0, 2)) ||
    Id("permis").value[2] != "/" ||
    !isNum(Id("permis").value.substr(2, 5))
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
    erer += "Select a sex ! \n"
  }

  if (err.length > 0) {
    alert(err)
    return false
  }
  return true
}

alert("hello world")
