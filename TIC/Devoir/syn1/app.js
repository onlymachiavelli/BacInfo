const Id = (id) => document.getElementById(id)
const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]

const Name = (Nam) => document.getElementsByName(Nam)

const Imc = () => {
  alert(
    "Votre IMC est : " +
      String(Number(Id("poid").value) / Number(Id("taille").value) ** 2)
  )
}
