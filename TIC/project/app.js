const Id = (id) => document.getElementById(id)
const Name = (namme) => document.getElementsByName(namme)

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

  if (myDatas.email.indexOf("@") !== -1 && myDatas.email.indexOf(".") !== -1) {
    let [dom, com] = myDatas.email.split(".")
    let [user, platform] = myDatas.email.split("@")
    platform = platform.split(".")[0]
    console.log(dom, com, user, platform)
    if (
      (!(com.toLowerCase() in ["fr", "com"]) && user.length < 4) ||
      !(
        platform.toLowerCase() in
        ["gmail", "outlook", "yahoo", "live", "proton"]
      )
    ) {
      error += "email is not valid \n"
    }
  } else {
    error += "email is not valid \n"
  }
  if (myDatas.clas === null) {
    error += "select your class !  \n"
  }
  if (error.length > 0) {
    alert(error)
  }
  return error.length > 0 ? false : true
}

const Click = () => {
  if (check()) {
    alert("Good")
  }
}

Id("btn").addEventListener("click", () => {
  Click()
})
