const Id = (id) => document.getElementById(id);
const Name = (namme) => document.getElementsByName(namme);

const verif = () => {
  let err = "";

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
};
