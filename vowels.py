user_input  = input("Enter the String: ").lower()
counter = 0

for i in user_input:
    if i in ['a','e','i','o','u']:
        counter+=1
print("Count is:",counter)
