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
  if (myDatas.name.length < 4 && myDatas.name.indexOf(" ") == -1)
    error += "name is not valid \n"

  if (error.length !== 0) {
    alert(error)
  }
  return error.length > 0 ? false : true
}

const Click = () => {
  if (!check()) {
    alert("Form is not valid")
  } else {
  }
}

Id("checkBTN").addEventListener("click", () => {
  check()
})
