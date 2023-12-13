#gues the numba


import random

didWin = False


print("Hi! Lets play a game!\nI am going to choose a number from 1 to 100, and you will try to guess it.\nI will respond with too high or too low depending on your answer.")


randInt = random.randrange(1, 100)

while didWin != True:
    x = int(input("Enter a number:\n"))
    if x == randInt:
        print("Correct")
        didWin = True
        playAgain = input("\nPlay again?(Y/N):\n")
        if playAgain == "Y":
            randInt = random.randrange(1, 100)
            didWin = False
        else:
            break
    elif x > randInt:
        print("Too High")
    elif x < randInt:
        print("Too low")
        

