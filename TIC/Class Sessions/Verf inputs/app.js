const Class = (cl, ind) => document.getElementsByClassName(cl)[ind]

const Id = id => document.getElementById(id)





const Verf = () =>{
    res = ``
    if(Id("name").value.length > 0 && Id("name").value.indexOf(" ") !== -1) res += "Good Name \n" 
    else res += "Invalid name \n"
    if (Id("cin").value.length === 8 && (Id("cin").value.charAt(0) === "0" || Id("cin").value.charAt(0) ==="1") && !isNaN(Id("cin").value)) res += "Good CIN input"
    else res += "invalid cin input"
    alert(res)
}

