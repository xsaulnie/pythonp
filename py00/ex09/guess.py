import sys
import random

if (len(sys.argv) != 1):
    print("ERROR")
    sys.exit()

secret = random.randint(1, 99)

cmpt = 0

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood Luck!")
while True:
    cmpt = cmpt + 1
    number = input("What's your guess between 1 and 99?\n")
    if (number == "exit"):
        print("Goodbye!")
        sys.exit()
    elif (number.isdigit() == False):
        print("That's not a number.")
    elif (int(number) > secret):
        print("Too high!")
    elif (int(number) < secret):
        print("Too low!")
    else:
        print("Congratulations, you've got it!")
        break
if (secret == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if (cmpt == 1):
    print("Congratulation! You got it on your first try!")
else:
    print(f"You won in {cmpt} attempts!")
