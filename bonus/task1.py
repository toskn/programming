# Если пользователь вводит что-то кроме цифр, то значения будут разбиваться или удаляться.
# Пока не закончил, еще не сделал для отрицательных значений

import re

i = 0
inputted = ""
while i == 0:
    a = input()
    if a == "":
        i += 1
    else:
        inputted = inputted + " " + a
inputted = list(filter(None, re.split('\D', inputted)))
inputted2 = []
for ii in inputted:
    if ii != '':
        inputted2.append(int(ii))


def sum_of_numbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum_of_numbers(numbers[1:])


print((sum_of_numbers(inputted2))/len(inputted2))
print(min(inputted2))
print(max(inputted2))
