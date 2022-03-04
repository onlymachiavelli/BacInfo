const Id = (id) => document.getElementById(id)
const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Name = (nam) => document.getElementsByName(nam)
const checkSignUp = () => {
  const arr = Name("sex").value
  console.log(arr)
}

const checkLogin = () => {}
