import re
i = 0
three_letter = 0
one_letter = 0
with open("/Users/egor/Documents/GitHub/KILI/LiveCorpus/family.2.txt", encoding="utf-8") as text:
    text = text.read()
    text = list(filter(None, re.split('\W', text)))
    for i in text:
        if len(i) == 3:
            three_letter += 1
        if len(i) == 1:
            one_letter += 1
    if one_letter == 0:
        print("Слов длины 1 в тексте нет")
    else:
        print(three_letter / one_letter)


