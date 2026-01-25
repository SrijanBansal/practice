import string

def has_special_char(s):
    return any(char in string.punctuation for char in s)


print(has_special_char("hello1234"))
