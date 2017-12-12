i = 0
inputted = ""
b = []

while i == 0:
    a = input()
    if a == "":
        i += 1
    else:
        inputted = inputted + " " + a
inputted = inputted.split()

with open("/Users/egor/Documents/GitHub/programming.git/EXAM/Ozhegov.txt", encoding="utf-8") as text:
    text = text.read()
    text = text.replace("|", " | ")
    text = text.split("\n")
    for i in range(len(text)):
        a = text[i].split(" ")
        b.append(a)
print(b)
for ii in range(len(inputted)):
    if inputted[ii] in b[ii][0] is True:
        #print(b[ii][0] + "-" + b[ii][3] + "-" + b[ii][1])
    #тут написать про то, что выводить текст между определенными палками
    else:
        print("there is no such a word in the dictionary")
