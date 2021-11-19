function Id(id) {
  return document.getElementById(id)
}

function Name(name) {
  return document.getElementsByName(name)
}

function Email(myEmail) {
  if (myEmail.idexOf("@") === -1 || myEmail.idexOf(".") === -1) return false

  const [a, b] = myEmail.split("@")
  const [c, d] = b.split(".")
}
