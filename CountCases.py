s = "ProGramminG"
l_counter  = 0
u_counter  = 0
for ch in s:
    if ch.isalpha():
        if ch.isupper():
            u_counter +=1
        else:
            l_counter+=1

print(l_counter)
print(u_counter)
