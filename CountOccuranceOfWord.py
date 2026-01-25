s = "python is easy and python is powerfull and is also readable"
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word,0) +1
    
print(freq)
