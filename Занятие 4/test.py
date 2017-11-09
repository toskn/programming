s = 'oh, hi mark'
list_from_string = list(s)
print(list_from_string)

students = ['Аня', 'Elya', 'anya']
students.append('sofia')


# разница extend и  +
print(students[1][0])
del students[2]

students.insert(2, 'Egor')
print(', '.join(students))


a = list('abcdefgh')
for i in range (0, len(a), 2):
    print(a[i])

students = ['anya', 'sofya', 'aleksey maschina STARCHENKO', 'egor', 'daniil']
for x in range (1, len(students)):
    if len(students[x]) > len(students[x-1]):
        print(students[x])

for y in range (0, len(students)-1, 2):
    students[y], students[y+1] = students[y+1], students[y]
    print(students)

