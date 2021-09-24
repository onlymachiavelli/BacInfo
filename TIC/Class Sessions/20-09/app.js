const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Id = (id) => document.getElementById(id)
//Initial FRAME SOURCE
Class("comp", 0).src = "welc.html"

Class("link", 0).addEventListener("click", () => {
  alert("tst")
})
