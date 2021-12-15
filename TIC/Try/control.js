const Name = (nam) => document.getElementsByName(nam)

const Id = (id) => document.getElementById(id)

const isChecked = () => {
  let check = false
  let i = 0
  do {
    if (Name("sex")[i].checked) check = true
    console.log(check)
    i++
  } while (i != Name("sex").length)

  return check
}

const Check = () => {
  alert(isChecked())
}
