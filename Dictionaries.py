
def load_words():
    words ={}
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if not word in words:
             words[word] = word

    return words

def histogram(sentence):
    d = dict()
    for letter in sentence:
        d[letter] = d.get(letter,0) + 1

    return d

def reverse_lookup(histogram, value):
    keys = []
    for key in histogram:
        if histogram[key] == value:
            keys.append(key)
    return keys

def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def print_histogram(histogram):
    keys = list(histogram.keys())
    keys.sort()

    for letter in keys:
        print(letter, histogram[letter])


print(len(load_words()))

h = histogram('lorem ipsum dolor sit amet')
print_histogram(h)
print(reverse_lookup(h,2))
print(reverse_lookup(h,7))
print(inverse_dict(h))
