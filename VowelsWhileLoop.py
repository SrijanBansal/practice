check  = input().lower()

index = 0
count = 0

while index < len(check):
    if check[index] in 'aeiou':
        count += 1
    index += 1

print(count)
