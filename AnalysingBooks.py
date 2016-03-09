import string
from collections import defaultdict

def analyse_word_usage(filename):

    wordCounts = dict()

    fin = open(filename)
    for line in fin:
        line = line.strip()
        words = line.split()
        for word in words:
            word = clean_word(word)
            wordCounts[word] = wordCounts.get(word,0) + 1

    return wordCounts

def clean_word(word):
    newWord = word
    # is this unnecessary?
    newWord = newWord.strip()

    new_string = ''

    for char in newWord:
        if is_not_punct_char(char):
            new_string = new_string+char

    return new_string.lower()

def is_not_punct_char(char):
    return not is_punct_char(char)

def is_punct_char(char):
    return char in string.punctuation

def unique_value(histogram):
    uniqueValues = list(set(list(histogram.values())))
    return uniqueValues.sort()


def invert_index(histogram):
    inverted_index = defaultdict(list)

    for key,value in histogram.items():
        inverted_index[value].append(key)

    return inverted_index


def get_top_entries(entries, inverted_index):

    printedentries = 0

    sortedKeys = list(inverted_index.keys())
    sortedKeys.sort(reverse = True)

    for key in sortedKeys:
        value = inverted_index[key]
        # go through the highest entries, until we hit the magic number
        values = list(value)
        values.sort()
        for entry in values:
            if printedentries >= entries:
                break

            print(printedentries +1, entry ,key)
            printedentries += 1

        #this feels ugly
        if printedentries >= entries:
            break

histogram = analyse_word_usage('pg1661.txt')
inverted_index = invert_index(histogram)
get_top_entries(50,inverted_index)
