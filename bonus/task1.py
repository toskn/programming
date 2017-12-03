inputted = []


while True:
    a = input()
    if a == "":
        break
    else:
        inputted.append(a)


def numbered(x):
    xx = ""
    for i in range(len(x)):
        if x[i] == "-" and xx == "":
            xx += "-"

        elif x[i].isdigit():
            xx += x[i]
        elif (x[i] == "." or x[i] == ",") and ((len(xx) >= 1 and xx[0].isdigit()) or (len(xx) >= 2 and xx[0] == "-")):
            xx += "."
    if xx == "" or xx == "-":
        xx = 0
    else:
        xx = float(xx)
    return xx


for item in range(len(inputted)):
    inputted[item] = numbered(inputted[item])

print(sum(inputted)/len(inputted), max(inputted), min(inputted))
