a = input()


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


a = numbered(a)
print('Градусы по Фаренгейту: ', a * (9 / 5) + 32)
print('Градусы по Кельвину: ', a + 273.15)
