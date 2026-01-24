s= "programming"
vowels = "aeiou"

counter=0

for ch in s:
    if ch.isalpha() and ch not in vowels:
        counter+=1

print(counter)
        
