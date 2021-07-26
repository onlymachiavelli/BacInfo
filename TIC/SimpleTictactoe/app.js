
const Class = cl => document.getElementsByClassName(cl)[0]
let User = ""

const Color = (button) => {
    if (button.innerHTML == "X") button.style.backgroundColor = "#880453"
    else if (button.innerHTML == "O") button.style.backgroundColor = "#885f04"
    else button.style.backgroundColor = "#7d0488"
}
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
    //yeah sorry about that i wanted to keep it simple so u can understand ! 
    if (
        Class("btn0").innerHTML == symbol && Class("btn1").innerHTML == symbol && Class("btn2").innerHTML == symbol ||
        Class("btn3").innerHTML == symbol && Class("btn4").innerHTML == symbol && Class("btn5").innerHTML == symbol ||
        Class("btn6").innerHTML == symbol && Class("btn7").innerHTML == symbol && Class("btn8").innerHTML == symbol ||
        Class("btn0").innerHTML == symbol && Class("btn3").innerHTML == symbol && Class("btn6").innerHTML == symbol ||
        Class("btn1").innerHTML == symbol && Class("btn4").innerHTML == symbol && Class("btn7").innerHTML == symbol ||
        Class("btn2").innerHTML == symbol && Class("btn5").innerHTML == symbol && Class("btn8").innerHTML == symbol ||
        Class("btn0").innerHTML == symbol && Class("btn4").innerHTML == symbol && Class("btn8").innerHTML == symbol ||
        Class("btn2").innerHTML == symbol && Class("btn4").innerHTML == symbol && Class("btn6").innerHTML == symbol
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
        Color(Class(index))
        if (End()) {
            alert("DRAW")
            Start()
        }


        if (Winner(User)) {
            alert("Player " + User + " Just Won !")
            Start()

        }
        else {
            if (User == "X") User = "O"
            else User = "X"
        }


    }
}
