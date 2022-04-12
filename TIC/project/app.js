const Id = (id) => document.getElementById(id)
const Name = (namme) => document.getElementsByName(namme)

const checkEmail = (theEmail) => {
  if (
    theEmail.indexOf("@") !== -1 &&
    theEmail.indexOf(".") !== -1 &&
    theEmail.indexOf(".") > myDatas.email.indexOf("@") &&
    theEmail.length < 50
  ) {
    let [dom, com] = theEmail.split(".")
    let [user, platform] = theEmail.split("@")
    platform = platform.split(".")[0]
    if (
      ["fr", "com"].indexOf(com.toLowerCase()) === -1 ||
      user.length < 4 ||
      ["gmail", "outlook", "yahoo", "live", "proton"].indexOf(
        platform.toLowerCase()
      ) === -1 ||
      platform.indexOf(".") !== -1
    ) {
      return false
    }
  } else {
    return false
  }

  return true
}

const check = () => {
  const myDatas = {
    nom: Name("name")[0].value,
    gen: Name("sex"),
    email: Name("email")[0].value,
    clas: Name("nc")[0].value,
  }
  let error = ""
  if (myDatas.nom.length <= 4 || myDatas.nom.indexOf(" ") === -1) {
    error += "name is not valid \n"
  }
  if (!myDatas.gen[0].checked && !myDatas.gen[1].checked) {
    error += "you have to choose your sex ! \n"
  }

  if (!checkEmail(myDatas.email)) {
    error += "Invalid Email ! \n"
  }

  if (myDatas.clas === null) {
    error += "select your class !  \n"
  }
  if (error.length > 0) {
    alert(error)
  }
  return error.length > 0 ? false : true
}

const checkUp = () => {
  let error = ""
  if (Number(Name("id")[0].value) <= 0) {
    error += "invalid ID ! \n"
  }

  if (!checkEmail(Name("email")[0].value)) {
    error += "Invalid Email ! \n"
  }

  if (error.length > 0) {
    alert(error)
  }

  return error.length > 0 ? false : true
}
