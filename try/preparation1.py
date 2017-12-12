with open("/Users/egor/Documents/GitHub/programming.git/try/freq.txt", encoding="utf-8") as text:
    text = text.read()
    text = text.split("\n")
    for i in range(len(text)):
        a = text[i].split()
        if len(a) >= 5 and a[4] == "перех":
            print(text[i])
