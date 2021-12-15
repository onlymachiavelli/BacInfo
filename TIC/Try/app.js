const Name = (nam) => document.getElementsByName(nam)

const check = (str) => {
  const alpha = "abcdefghijklmnopqrstuvwxyz "
  let check = true
  let i = 0
  do {
    if (alpha.indexOf(str[i]) === -1) check = false
    i++
  } while (i < str.length || check)

  return check
}

console.log(check("hello world"))
