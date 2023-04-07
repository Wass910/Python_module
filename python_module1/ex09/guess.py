import sys
import string
import random

if __name__ != "__main__":
    sys.exit()

nb_to_find = random.randint(1, 99)
nb_try = 0
print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
print()

while 1:
    proposition = input("What's your guess between 1 and 99?\n>> ")
    try :
        nb = int(proposition)
    except:
        if proposition == "exit":
            print("Goodbye !")
            quit()
        print("Please enter a valid answer.")
        nb_try = nb_try + 1
    else:
        nb_try = nb_try + 1
        if nb > nb_to_find:
            print("Too High !")
        elif nb < nb_to_find:
            print("Too Low !")
        else:
            if (nb == 42):
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if nb_try == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulation You Won !")
                print(f"You Won In {nb_try} attempts!")
            quit()