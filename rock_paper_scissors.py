import random

computer_score = 0
user_score = 0


options = ["rock", "paper", 
"scissors"]

while True:
    user_input = input(" Enter rock/ paper / scissors or q to quit" ).lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_num =  random.randint(0, 2)
    computer_pick = options[random_num]

    if user_input == computer_pick:
        print(f" you have picked {user_input} and computer has picked {computer_pick} so no points")
    elif user_input == "rock" and computer_pick == "paper":
        print(f"you have picked {user_input} and computer has picked {computer_pick} \n so computer won")
        computer_score += 1
    elif  user_input == "paper" and computer_pick == "rock":
        print(f" you have picked {user_input} computer has picked {computer_pick} so you won")
        user_score += 1
    elif computer_pick == "scissors"  and user_input == "rock":
        print(f"you have picked  {user_input}  and computer has picked  {computer_pick}   so you won")
        user_score += 1
    elif user_input == "rock" and computer_pick == "scissors":
        print(f"you have picked  {user_input}   and computer has picked  {computer_pick} so computer won ")
        computer_score += 1
    elif user_input == "paper"  and computer_pick == "scissors":
        print(f" you have picked  {user_input}   computer has picked  {computer_pick}  so computer won")
        computer_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print(f"you have picked  {user_input}   computer has picked   {computer_pick}   so you won")
        user_score +=1


print(f" Your  score is {user_score}")
print(f"computer score is  {computer_score}")

if computer_score ==0 and user_score == 0:
    quit()
elif computer_score > user_score:
    print("computer won the game! ")
elif computer_score < user_score:
    print("You won the game!")
else:
    print("game ends in draw")

print(" Good bye!")