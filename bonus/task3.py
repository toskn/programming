import re
import sys


def pig_latin():
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z",
                  "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    a = str(input("Type a word or a phrase: "))
    a = list(filter(None, re.split('(\w)', a)))
    if a[0] not in consonants:
        b = "".join(a) + "ay"
        print(b)
        sys.exit()
    if a[0] and a[1] in consonants:
        a.append(a[0])
        a.append(a[1])
        a.remove(a[0])
        a.remove(a[0])
        b = "".join(a) + "ay"
        print(b)
        sys.exit()
    if a[0] in consonants and a[1] not in consonants:
        a.append(a[0])
        a.remove(a[0])
        b = "".join(a) + "ay"
        print(b)
        sys.exit()


pig_latin()
