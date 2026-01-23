s = "programming"

result = ""

for dup in s:
    if dup not in result:
        result += dup
print(result)
