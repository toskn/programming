with open("/Users/egor/Documents/GitHub/programming.git/EXAM/Ozhegov.txt", encoding="utf-8") as text:
    text = text.read()
    text = text.replace("|", " ")
    text = text.split("\n")
    for i in range(len(text)):
        a = text[i].split()
        try:
            if len(a[0]) >= 20:
                print(a)
        except IndexError:
            print()
