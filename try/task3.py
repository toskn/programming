consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
vowel = ['a', 'e', 'i', 'o', 'y']
a = input()
x = 0
a = a.split()

def pig_latin_consonant(inputted):
for i in range(len(consonant)):
    if consonant[i] == inputted[0:i:]:
        x = x + 1
    inputted = inputted[x+1::] + inputted[0:x+1:] + 'ay'
    print(inputted
          )
