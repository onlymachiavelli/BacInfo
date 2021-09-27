const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Id = (id) => document.getElementById(id)

const setInpType = (input, button) => {
  if (Class(input, 0).type === "text") {
    Class(input, 0).type = "password"
    Class(button, 0).innerHTML = `<i class="fa fa-eye" aria-hidden="true"></i>`
  } else {
    Class(input, 0).type = "text"
    Class(
      button,
      0
    ).innerHTML = `<i class="fa fa-eye-slash" aria-hidden="true"></i>`
  }
}

//initial val simple
