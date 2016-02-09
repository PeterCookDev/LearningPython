def nested_sum(numbers):
	currentTotal = 0
	for i in numbers:
		if(isinstance(i, list)):
			currentTotal += nested_sum(i)
		else:	
			currentTotal += i
	return currentTotal


def capitalize_all(sentence):
    res = []
    for word in sentence:
        res.append(word.capitalize())
    return res

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def cumulative_sum(numbers):
    res = []
    cumsum = 0
    for number in numbers:
        cumsum += number
        res.append(cumsum)

    return res

print(nested_sum([1,2,3,[4,5,[6,7],[8]]]))
print(cumulative_sum([10,20]))
print(only_upper('ABcdEfGhI'))
print(capitalize_all(['lorem','ipsum']))
print(capitalize_all('lorem ipsum'))

