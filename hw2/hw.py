a = input('введите слово кириллицей ')
a = a[::-1]
b = len(a)
i = 0
while i < b:
    if 'я' in a:
        i = a.index('я')
        a = a[:i] + a[i + 1:]
    if 'з' in a:
        i = a.index('з')
        a = a[:i] + a[i + 1:]
    i += 1
print(a)