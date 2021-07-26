
const Class = cl => document.getElementsByClassName(cl)[0]
let User = ""

const Start = () => {
    let r = Math.floor(Math.random() * 2)
    if (r == 0) User = "X"
    else User = "O"
    alert(User + " Start !")
    Class("container").innerHTML = ``
    for (let i = 0; i < 9; i++) {
        Class("container").innerHTML += `<button class="btn${i}" onclick="Game('btn${i}')">E</button>`
        if (i === 2 || i == 5) Class("container").innerHTML += `<br/>`
    }
}
Start()

const Winner = (symbol) => {
    if (
        Class("btn0") == symbol && Class("btn1") == symbol && Class("btn2") == symbol
    ) return true
}



const End = () => {
    for (let i = 0; i < 9; i++) {
        if (Class("btn" + i).innerHTML == "E") return false
    }
    return true
}

const IsEmpty = (ind) => {
    if (Class(ind).innerHTML == "E") return true
    else return false
}
const Game = (index) => {
    if (!IsEmpty(index)) alert("token place mother fucker")
    else {
        Class(index).innerHTML = User

        if (End()) {
            alert("GLUTCH")
            Start()
        }
        if (Winner(User)) {
            alert("Player " + User + " Just Won !")
            Start()
        }


        if (User == "X") User = "O"
        else User = "X"

    }
}
