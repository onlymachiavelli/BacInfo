const Id = (id) => document.getElementById(id);

const Name = (namme) => document.getElementsByName(namme);

const exist = (element, arr) => {
  for (let i = 0; i < arr.length; i++) {
    if (element === arr[i]) return true;
  }
  return false;
};

const cYear = () => {
  let yr = new Date().getFullYear();
  Id("year").value = yr;
};

const check = () => {
  let err = "";

  let thone = new Array(1, 3, 5, 7, 8, 10, 12);
  let thirty = new Array(4, 6, 9, 11);

  if (Number(Id("month").value) < 1 || Number(Id("month").value) > 12) {
    err += "month out of intervale \n";
  } else {
    if (exist(Number(Id("month").value), thone)) {
      if (Number(Id("day").value) > 31 || Number(Id("day").value) < 1) {
        err += "Invalid Day \n";
      }
    } else if (exist(Number(Id("month").value), thirty)) {
      if (Number(Id("day").value) > 30 || Number(Id("day").value) < 1) {
        err += "Invalid Day \n";
      }
    } else {
      //assuming the month is 2
      if (Number(Id("year").value) % 4 === 0) {
        if (Number(Id("day").value) > 29 || Number(Id("day").value) < 1) {
          err += "Invalid Day \n";
        }
      } else {
        if (Number(Id("day").value) > 28 || Number(Id("day").value) < 1) {
          err += "Invalid Day \n";
        }
      }
    }
  }

  if (Id("peace").selectedIndex === 0) {
    err += "Invalid Choice \n";
  }
  if (Id("salle").selectedIndex === 0) {
    err += "Invalid Choice \n";
  }

  if (err.length > 0) {
    alert(err);
    return false;
  }
  return true;
};
