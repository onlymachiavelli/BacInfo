const Id = (id) => document.getElementById(id)
const Name = (namme) => document.getElementsByName(namme)

const check = () => {
  const myDatas = {
    nom: Name("name")[0].value,
    gen: Name("sex"),
    email: Name("email")[0].value,
    clas: Name("nc"),
  }
  let error = ""
  if (myDatas.nom.length <= 4 || myDatas.nom.indexOf(" ") === -1) {
    error += "name is not valid \n"
  }
  if (!myDatas.gen[0].checked && !myDatas.gen[1].checked) {
    error += "you have to choose your sex ! \n"
  }

  const [dom, com] = myDatas.email.split(".")
  const [user, platform] = myDatas.email.split("@")
  if (
    !(com.toLowerCase() in ["fr", "com"]) ||
    user.length < 4 ||
    !(platform.toLowerCase() in ["gmail", "outlook", "yahoo", "live", "proton"])
  ) {
    error += "email is not valid \n"
  }

  if (error.length > 0) {
    alert(error)
  }
  return error.length > 0 ? false : true
}

const Click = () => {
  if (!check()) {
    alert("Form is not valid")
  } else {
    alert("good")
  }
}

Id("btn").addEventListener("click", () => {
  Click()
})
