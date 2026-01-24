s = "programming"
vowels = "aeiou"
result = ""

for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result+=ch
print(result)
