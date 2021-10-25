//تعرفش حرام عيش ولدي ؟

const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]

const Id = (id) => document.getElementById(id)
const Name = (namme) => document.getElementsByName(namme)
function isAlpha(str) {
  alpha = "abcdefghijklmnopqrstuvwxyz"
  str = str.toLowerCase()
  for (i = 0; i < str.length; i++) {
    if (alpha.indexOf(str[i]) === -1) return false
  }
  return true
}
const Verf = () => {
  res = ``
  Message = ""
  checkm = true
  if (Id("name").value.length > 0 && isAlpha(Id("name").value))
    res += "Good Name \n"
  else {
    res += "Invalid name \n"
    checkm = false
  }

  if (Id("lname").value.length > 0 && isAlpha(Id("lname").value))
    res += "Good last Name \n"
  else {
    res += "Invalid last name \n"
    checkm = false
  }
  if (
    Id("cin").value.length === 8 &&
    (Id("cin").value.charAt(0) === "0" || Id("cin").value.charAt(0) === "1") &&
    !isNaN(Id("cin").value)
  )
    res += "Good CIN input \n "
  else {
    res += "invalid cin input \n"
    checkm = false
  }

  if (!Name("sex")[0].checked && !Name("sex")[1].checked) {
    res += "Choose one ! \n"
    checkm = false
  } else res += "hello it is checked \n"
  alert(res)

  if (checkm) {
    mr = ""
    if (Name("sex")[0].checked) mr = "Mr"
    else mr = "Miss"
    Message = `Hello ${mr} ${Id("name").value} ${
      Id("lname").value
    } the owner of ${Id("cin").value}`
    Id("msg").innerHTML = Message
  }
}
