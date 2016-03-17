import nltk

def load_book(filename):
    fin = open(filename)

    body = fin.read()
    tokens = nltk.word_tokenize(body)

    text = nltk.Text(tokens)

    return text


text = load_book('pg1661.txt')

print('Words ', len(text))
print('Distinct Words ',len(sorted(set(text))))

word = 'Watson'

print('Word',word)
print('Times word Appears', text.count(word))
print(text.concordance(word))
print(text.similar(word))

print(text.common_contexts(['Watson','Holmes']))
