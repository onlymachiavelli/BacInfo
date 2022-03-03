const Id = (id) => document.getElementById(id)
const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Name = (nam, id) => {
  return id >= 0
    ? document.getElementsByName(nam)[id]
    : document.getElementsByName(nam)
}

const checkSignUp = () => {
  const Arr = Name("sex", -1).value
  console.log(Arr[0].checked)
}

const checkLogin = () => {}

checkSignUp()
