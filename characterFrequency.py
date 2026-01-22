user_str = 'programming'

char_count = {}

for ch in user_str:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)
