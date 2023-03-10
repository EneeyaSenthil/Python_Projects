import random

max_range = input("Enter a number")

if max_range.isdigit():
    max_range = int(max_range)
    if max_range <= 0:
        print("please enter a number next time")
        quit()
else:
    print(" Numbers are only allowed ")
    quit()
rand_num = random.randint(0, max_range)
guesses = 0
while True:
    guesses += 1
    user_guesses = input("make a guess")
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print("Please enter a number next time")
        continue


    if user_guesses == rand_num:
        print("You got it right! ")
        break
    elif user_guesses > rand_num:
        print("You are above the number! ")
    else:
        print("You are below the number! ")

print("You got it in " + " "+ str(guesses))