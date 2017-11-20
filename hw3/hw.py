a = input()
i = 0
print(a)
while (i + 1) < len(a):
    a1 = a[i+1:] + a[0:i+1:]
    i = i + 1
    print(a1)

