
str = 'text to tuple, del punct. and space, search word max len'
print(str)

word = str.split()
word_p = [i.strip('.:;?,-!') for i in word]

t = tuple(word_p)
print(t)

word_max = max(t, key=len)
print(word_max)
