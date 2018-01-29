import re


def open_file_to_list():
    i = str(input('Type the name of the .txt file: '))
    filename = "./" + i + ".txt"
    with open(filename, encoding="utf-8") as file:
        file = file.read()
        file = list(filter(None, re.split('\W', file)))
        return file


def hood_check(file):
    freq_dict = {}
    for x in range(len(file)):
        if file[x][-4::] == "hood" or file[x][-5::] == "hoods":
            if file[x] in freq_dict:
                freq_dict[file[x]] += 1
            else:
                freq_dict[file[x]] = 1
    return freq_dict


def word_gen(freq_dict):
    word_gen_list = []
    for word in freq_dict:
        if word[-6::] == "lihood":      # для правильного выделения основ в словах типа likelihood
            word_gen_list.append(word[0:-6:])
        elif word[-4::] == "hood":
            word_gen_list.append(word[0:-4:])
        else:
            word_gen_list.append(word[0:-5:])  # слова на ihood и hoods попадают в эту группу
    return word_gen_list


def word_amount(freq_dict):
    word_amount_list = sum(list(freq_dict.values()))
    return word_amount_list


def min_freq(freq_dict):
    volume = list(freq_dict.values())
    key = list(freq_dict.keys())
    return key[volume.index(min(volume))]


print("Word genesis: " + str(word_gen(hood_check(open_file_to_list()))))
# придется вводить несколько раз название файла из-за того, что весь код в функциях
print("Amount of words ending with '-hood': " + str(word_amount(hood_check(open_file_to_list()))))
print("Word(-s) with minimal frequency: " + str(min_freq(hood_check(open_file_to_list()))))
