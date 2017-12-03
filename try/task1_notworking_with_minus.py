# Если пользователь вводит что-то кроме цифр, то значения будут разбиваться или удаляться.
import re
# Введем переменные
i = 0
inputted = ""
inputted2 = []

# Пользователь вводит переменные
while i == 0:
    a = input()
    if a == "":
        i += 1
    else:
        inputted = inputted + " " + a
        inputted.replace("-", " -")

# удаляем все символы кроме цифр и записываем цифры в новый список inputted_clear.
# Элементы делятся по чему-либо кроме цифры.
inputted_clear = list(filter(None, re.split('\D', inputted)))

# берем изначальную строку, из нее делаем список, в списке ищем минус, если следующий элемент - цифра или число, то
# удаляем один элемент, который равен числу после минуса из списка inputted_clear, а вместо него вписываем элемент с
# минусом перед ним
inputted = inputted.split(" ")
for x in range(len(inputted)):
    if inputted[x] == "-":
        if inputted[x+1].isdigit is True:
            i = inputted[x+1]
            for a in range(len(inputted_clear)):
                if i == inputted_clear[a]:
                    del inputted_clear[a]
                    i = inputted[x] + i
                    inputted_clear.append(i)
    continue


for ii in inputted_clear:
    if ii != '':
        inputted2.append(int(ii))

'''
def sum_of_numbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum_of_numbers(numbers[1:])
'''

print((sum(inputted2))/len(inputted2))
print(min(inputted2))
print(max(inputted2))
