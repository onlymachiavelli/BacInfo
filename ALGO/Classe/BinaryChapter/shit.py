def word():
    quit = False
    while not quit:
        word = input("Entrer le mot !")
        quit = 1 < len(word) <= 8
    return word


def indexOf(structure, element):
    found = False
    index = 0
    while not found and index < len(structure):
        found = structure[index] == element
        index = index + 1
    if found:
        return index
    return -1


def playerTwo(theWord):

    win = False
    wordC = ""
    print(wordC)
    for i in range(1, len(theWord)):
        wordC = wordC + "-"
    wordC = theWord[0] + wordC
    tries = 0
    while tries < len(wordC) and not win:
        print("Le mot est : ", wordC)
        print("Essaye ", i)
        answer = input()
        li = []
        for i in range(len(wordC)):
            li.append(wordC[i])
        i = 0

        while (i < len(theWord) and i < len(answer)):
            if answer[i].upper() == theWord[i].upper():
                li[i] = theWord[i]
            i = i + 1
        wordC = ""
        for i in range(len(li)):
            wordC = wordC + li[i]

        win = indexOf(wordC, "-") == -1
        tries = tries + 1
        print(tries)
    if win:
        print("Winner winner chicken dinner !")
    else:
        print("Looser Looser !")

    print("le mot est ", theWord)


theWord = word()
for i in range(100):
    print("---------------------------------")
playerTwo(theWord)
