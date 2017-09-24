filename = open('romeo.txt')
file = filename.read()
words = file.split()
key_words = []
for word in words:
    if  word in key_words:
        continue
    else:
        key_words.append(word)
key_words.sort()
print(key_words)