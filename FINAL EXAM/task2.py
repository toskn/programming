import os
import re


directory = './'
file_list = os.listdir(directory)
os.chdir(directory)


def open_files(i):
    filename = file_list[i]
    with open(filename, encoding="utf-8") as file:
        file = file.read()
    return file


W = dict()
for i in range(len(file_list)):
    file = open_files(i)

    words = re.split(' ', file)
    for word in words:
        if ('А' <= word[0] <= 'Я'):
            if word in W.keys():
                W[word] += 1
            else:
                W[word] = 1

for key in W.keys():
    print(str(key) + '\t' + str(W[key]))

#вообще не о том, я поздно сообразил про теги, уже когда набросал тут.