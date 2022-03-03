const Id = (id) => document.getElementById(id)
const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Name = (nam, id) => {
  return id
    ? document.getElementsByName(nam)[id]
    : document.getElementsByName(nam)
}

const checkSignUp = () => {
  const Arr = Name("sex").value
  console.log(Arr)
}

const checkLogin = () => {}

checkSignUp()
