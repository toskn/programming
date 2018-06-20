import re


# 1 task


def open_file_split():
    i = str(input('Type the name of the .xml file: '))
    filename = "./" + i + ".xml"
    with open(filename, encoding="utf-8") as file:
        file = file.read()
        file = file.split("<body>")
        file = file[1].split("</body")
        return file[0]


def write_symbol_amount(file):
    with open("1answer.txt", "w", encoding="utf-8") as f:
        f.write(str(len(file)))


write_symbol_amount(open_file_split())


# 2 task

def file_to_dict(file):
    freq_dict = {}
    file = re.findall(r"""\bgr="\w*"\b""", file, re.IGNORECASE)
    for x in range(len(file)):
        if file[x][:4] == """gr=""""":
            file[x].replace(file[x], file[x][3:])
    for x, i in range(len(file)):
        if file[x] == file[i]:
            freq_dict[file[x]] += 1
    for x in range(len(file)):
        if freq_dict[file[x]] == 0


# я не успел, но тут дальше надо проверить на повторы в словаре - последний цикл.
# Потом открыть, как для перовго задания файл и записать туда по порядку значения используя этот модуль:

def max_freq(freq_dict):
    volume = list(freq_dict.values())
    key = list(freq_dict.keys())
    return key[volume.index(max(volume))]


open_file_split()