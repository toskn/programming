i = 0
ii = 0
iii = 0
inputted = ""
while i == 0:
    a = input()
    if a == "":
        i += 1
    else:
        inputted = inputted + " " + a
inputted = inputted.split(" ")


for ii in range(len(inputted)):
    if len(inputted[ii]) < ii:
        inputted[ii] = inputted[ii][ii+1::]
    else:
        inputted[ii] = ""


with open("answer.txt", "w", encoding="utf-8") as a:
    a.write("\n")
    for iii in range(len(inputted)):
        a.write(inputted[iii]+"\n")
