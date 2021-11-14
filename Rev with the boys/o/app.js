function Id(id) {
  return document.getElementById(id)
}

function Class(cls, id) {
  return document.getElementsByClassName(cls)[id]
}

function isUpper(Mahrez) {
  alpha = "ABCDEFGHIIJKLMNOPQRSTUVWXYZ"
  for (let i = 0; i < Mahrez.length; i++) {
    if (alpha.indexOf(Mahrez[i]) === -1) return false
  }

  return true
}
function isAlpha(myString) {
  alpha = "abcdefghijklmnopqrstuvwxyz"
  for (let i = 0; i < myString.length; i++) {
    if (alpha.indexOf(myString[i].toLowerCase()) === -1) return false
  }
  return true
}
function Name(myName) {
  if (myName.length === 0) return false
  if (myName.indexOf(" ") !== -1) return false
  if (!isUpper(myName[0]) || !isAlpha(myName)) return false
  return true
  // ! manetha false manetha el bar mtaa el haja hedhika manetha l opposite mteha
}

function Date(myDate) {
  if (myDate.length !== 10) return false

  let fullDate = myDate.split("/")
  if (fullDate.length !== 3) return false
  for (let i = 0; i < fullDate.length; i++) {
    if (i < 2) {
      if (fullDate[i].length !== 2) return false
    } else {
      if (fullDate[i] !== 4) return false
    }
    for (let j = 0; j < fullDate[i].length; j++) {
      if (isNaN(fullDate[i][j])) return false
    }
  }

  return true
}
function Sex() {
  let man = Id("man")
  let woman = Id("woman")
  if (!man.checked && !woman.checked) return false
  return true
}

function Check() {
  if (Name(Id("name").value)) alert("Good name")
  else alert("its not a good name ")
  if (Name(Id("lname").value)) alert("Good last name")
  else alert("Bad last name")
  if (Date(Id("date").value)) alert("Good date")
  else alert("Bad date")

  sextype = ""
  if (Sex()) {
    if (Id("man").checked) sextype = "Man"
    else sextype = "Woman"

    alert(sextype)
  } else alert("Bad sex choosing")
}
