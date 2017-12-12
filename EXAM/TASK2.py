ant_amount = 0
b = []
with open("/Users/egor/Documents/GitHub/programming.git/EXAM/Ozhegov.txt", encoding="utf-8") as text:
    text = text.read()
    text = text.split("\n")
    for i in range(len(text)):
        a = text[i].split("|")
        b.append(a)
    for ii in range(len(b)):
        if len(b[ii]) >= 3 and b[ii][2] != "":
            ant_amount += 1
print(ant_amount)

