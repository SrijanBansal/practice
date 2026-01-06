import random

get_random_number = input("Enter a number: ")

if get_random_number.isdigit():
    get_random_number = int(get_random_number)
    if (get_random_number) <= 0:
        print("Please enter number greater than zero next time")
        quit()

else:
    print("Please enter number next time")
    quit()

random_number = random.randint(0,get_random_number)
print(random_number)

counter=0
while True:
    counter += 1
    user_guess = input("Your Guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter number next time")
        continue
    
    if user_guess == get_random_number:
        print("Correct Guess")
        break
    else:
        print("Incorrect Guess")

print("You got in "+ str(counter) + " Guesses")

