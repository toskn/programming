import random
# chosen = random.randint(1, 2)
# местоимение наречие глагол прилагательное существительное

# не знаю как лучше указать пути в этой ситуации, поэтому оставлю те, что использовал

with open("/Users/egor/Documents/GitHub/programming.git/hw6/pronoms.txt", encoding="utf-8") as pronoms:
    pronoms = pronoms.read()
    pronoms = pronoms.split(",")
with open("/Users/egor/Documents/GitHub/programming.git/hw6/nouns.txt", encoding="utf-8") as nouns:
    nouns = nouns.read()
    nouns = nouns.split(",")
with open("/Users/egor/Documents/GitHub/programming.git/hw6/adverbs.txt", encoding="utf-8") as adverbs:
    adverbs = adverbs.read()
    adverbs = adverbs.split(",")
with open("/Users/egor/Documents/GitHub/programming.git/hw6/adjectives.txt", encoding="utf-8") as adjectives:
    adjectives = adjectives.read()
    adjectives = adjectives.split(",")
with open("/Users/egor/Documents/GitHub/programming.git/hw6/verbs.txt", encoding="utf-8") as verbs:
    verbs = verbs.read()
    verbs = verbs.split(",")
with open("/Users/egor/Documents/GitHub/programming.git/hw6/verbs1.txt", encoding="utf-8") as verbs1:
    verbs1 = verbs1.read()
    verbs1 = verbs1.split(",")


def pronom():

    return random.choice(pronoms)


def noun():

    return random.choice(nouns)


def adverb(word):

    return word + " " + random.choice(adverbs)


def adjective(word):
    if nouns.index(y) < 7:
        a = random.randint(0, 6)
        return adjectives[a] + " " + word

    if nouns.index(y) > 9:
        a = random.randint(7, 13)
        return adjectives[a] + " " + word
    if 7 <= nouns.index(y) <= 9:
        a = random.randint(14, 20)
        return adjectives[a] + " " + word


def verb(word):
        if pronoms.index(x) < 3:
            a = random.randint(0, 10)
            return word + " " + verbs[a]

        if pronoms.index(x) == 3:
            a = random.randint(11, 21)
            return word + " " + verbs[a]

        if pronoms.index(x) > 3:
            a = random.randint(22, 32)
            return word + " " + verbs[a]


x = pronom()
y = noun()


def rnd_sentence():
    return verb(adverb(x)) + " " + adjective(y)


def rnd1_sentence():
    return random.choice(verbs1) + " " + adjective(y)


sentence1 = rnd_sentence() + "?"
sentence1 = sentence1.capitalize()

sentence2 = rnd_sentence() + "!"
sentence2 = sentence2.capitalize()

sentence3 = "Не " + rnd_sentence() + "."

sentence4 = "Если ты это читаешь, то " + rnd_sentence() + "."

sentence5 = rnd1_sentence() + "."
sentence5 = sentence5.capitalize()

sentence_list = [sentence1, sentence2, sentence3, sentence4, sentence5]
random.shuffle(sentence_list)

print(" ".join(sentence_list))




