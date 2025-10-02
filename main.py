from random import randint


RPS_OPTIONS = [ "Rock", "Paper", "Scissors" ]


i = randint(0, 2)
computer_choice = RPS_OPTIONS[i]

print(computer_choice)

user_input = input("Please choose 'Rock', 'Paper', or 'Scissor's\n> ")
print()




user_wins = False
if user_input == "Rock" and computer_choice == "Scissors":
     user_wins = True
elif user_input == "Paper" and computer_choice == "Rock":
     user_wins = True
elif user_input == "Scissors" and computer_choice == "Paper":
    user_wins = True



message = f"The computer chose {computer_choice},"

if user_input == computer_choice:
     message +=  "you tied!!!"
elif user_wins:
     message += "you win!!! :))))"
else:
     message += "you lose.... "

print(message, end="\n")
