import random

get_random_number = input("Enter a number: ")

if get_random_number.isdigit():
    get_random_number = int(get_random_number)
    if get_random_number <= 0:
        print("Please enter number greater than zero next time")
        quit()
else:
    print("Please enter number next time")
    quit()

