const Id = (id) => document.getElementById(id)
const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Name = (nam, id) => document.getElementsByName(nam)[id]

const checkSignUp = () => {
  const Arr = Name("sex", 0)[0]
  console.log(Arr)
}

const checkLogin = () => {}

checkSignUp()
