//make js easier!
const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]
const Id = (id) => document.getElementsByClassName(id)

//Use Localstorage
const Get = (Key) => localStorage.getItem(Key)
const Add = (Key, Val) => localStorage.setItem(Key, Val)
const Clear = () => localStorage.clear()
const Delete = (Key) => localStorage.removeItem(Key)
//if()

let Container = Class("container", 0)
Class("addbtn", 0).addEventListener("click", () => {})
