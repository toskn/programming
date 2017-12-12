list_answer = []
ipm_sum = 0

with open("/Users/egor/Documents/GitHub/programming.git/try/freq.txt", encoding="utf-8") as text:
    text = text.read()
    text = text.split("\n")
    for i in range(len(text)):
        a = text[i].split()
        if len(a) >= 4 and a[2] == "част":
            list_answer.append(a[0])
            ipm_sum = ipm_sum + float(a[4])
            if len(a) == 6 and a[3] == "част":
                list_answer.append(a[0])
            ipm_sum = ipm_sum + float(a[4])
print(list_answer, ipm_sum)
