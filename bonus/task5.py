import re


def aig():
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z",
                  "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    a = str(input("Type a word or a phrase: "))
    a = list(filter(None, re.split('(\w)', a)))
    for i in range(len(a)):
        if a[i] in consonants:
            a[i] = a[i] + "aig"
    b = "".join(a)
    print(b)


aig()
