const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
Class("b", 0).style.display = "none"
Class("up", 0).addEventListener("click", () => {
  Class("upload", 0).click()
  Class("a", 0).style.display = "none"
  Class("b", 0).style.display = "block"
})
