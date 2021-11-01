//تعرفش حرام عيش ولدي ؟

//سنحاول ان نتكلم العربية

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

const Interest = () => {
  interest = ["Music", "Internet", "Sport"]
  res = `You are intrested in : `
  check = false

  for (i = 0; i < 3; i++) {
    if (Id(`int${i + 1}`).checked) {
      res += interest[i] + " ,"
      check = true
    }
  }

  if (check) return res

  return "You're intrested in Nothing"
}

const Phone = (number) => {
  for (i = 0; i < number.length; i++) {
    if (isNaN(number[i])) return false
  }
  if (Number(number[0]) <= 1) return false
  if (number.length !== 8) return false

  return true
}

const Email = (myEmail) => {
  if (myEmail.indexOf("@") === -1) return false
  if (!myEmail.endsWith(".com") || !myEmail.endsWith(".fr")) return false

  return true
}
const Verf = () => {
  let res = ``
  let Message = ""
  let checkm = true
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

  res += Interest() + "\n"
  if (Phone(Id("phonenumber").value)) res += "Good phone Number \n"
  else res += "Bad phone number \n"

  alert(res)

  if (checkm) {
    mr = ""
    if (Name("sex")[0].checked) mr = "Mr"
    else mr = "Miss"
    Message = `Hello ${mr} ${Id("name").value} ${
      Id("lname").value
    } the owner of ${Id("cin").value}`

    Message += Id("msg").innerHTML = Message
  }
}
