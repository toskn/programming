import re
import os
# это задание можно сделать используя библиотеки на  xml типа lxml и не выделять теги.
file_list = sorted(os.listdir('./'))


def open_files(i):
    q = 0
    a = ""
    filename = file_list[i]
    with open(filename, encoding="utf-8") as file:
        file = file.read()

# re.sub('<[^<]+>', "", file)

#start = '</ana>'
#end = '</w>'
        file = file.split("\t")
        while q < len(file)
        s = file[q]
# [s.find(start)+len(start):s.rfind(end)]
        a = a + s
    return a

# def making_title():


def cycle_opening():
    i = 0
    while i < 15:
        open_files(i)
        i = i + 1


cycle_opening()


# надо было просто выделить все, что между тегами /аna и /w, и все между тегом /w и "\t", а потом склеить в одну строку,
# изаписать в файл