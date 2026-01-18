import random

user_score = 0
computer_score = 0

options = ["rock","paper","scissors"]

while True:
    user_answer = input("Rock/Paper/Scissors or Q for quit ").lower()

    if user_answer == 'q':
        break
    if user_answer not in options:
        print("Select from Rock/Paper/Scissors")
        continue

    computer_choose = random.randint(0,3)
    computer_answer = options[computer_choose]
    print("Computer Chose ", computer_answer)

    if user_answer =="rock" and computer_answer == "scissors":
        print("User Wins")
        user_score+=1
    elif user_answer == "paper" and computer_answer == "rock":
        print("User Wins")
        user_score+=1
    elif user_answer == "scissors" and computer_answer == "paper":
        print("User Wins")
        user_score+=1
    else:
        print("Computer Wins")
        computer_score+=1
print("You won ", user_score,"times")
print("Computer won ", computer_score,"times")
print("Good Bye!")
