
def no_e(word):
    return 'e' in word.lower()


def no_e_in_file():
    lines = 0
    with_e = 0

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if(no_e(word)):
            with_e += 1

        lines +=1

    print(with_e * 100.0 / lines)

def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True


def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True


def uses_only(word, letters):
    #uses_all(letters, words)
    for letter in word:
        if letter not in letters:
            return False
    return True


def is_abecedarian(word):
    previousLetter = word[0]
    for letter in word:
        if letter < previousLetter:
            return False
        previousLetter = letter
    return True

def how_many_abecedarian_in_file():
    abecedarian = 0

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if(is_abecedarian(word)):
            abecedarian += 1
            print(word)
    print(abecedarian)


#no_e_in_file()
#print(avoids('abc','bc'))
#print(avoids('efg','ab'))

#print(uses_all("ab c","bcd"))
#print(uses_all("a bc","bc"))
#print(uses_all("ab c",""))

how_many_abecedarian_in_file()
