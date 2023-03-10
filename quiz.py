print("Hello Buddy! \n  Wellcome to this game!")
playing = input("Do you want to play this game? ")
if playing.lower()  != "yes":
    quit()

print("Okay! let's start playing")
score = 0
answer = input("who developed python? ")

if answer.title() == "Guido Van Rossum":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("Which keyword is used for function in Python language?")

if answer.lower() == "def":
    print("correct")
    score +=1
else:
    print("incorrect")

answer  = input(" Which symbol is used for function in Python language?")
if answer == "#":
    print("correct")
    score +=1
else:
    print("incorrect")
answer = input("Which functions can help us to find the version of python that we are currently working on? ")

if answer == "sys.version(1)":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("Which  construct helps to create an anonymous functions at runtime in python? ")
if answer == "lambda":
    print("correct")
    score +=1
else:
    print("incorrect")

print("you have got scored 5 out of" + str(score))