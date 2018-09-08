# Simple Projects found here. https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the
# -python-beginner/ This is project 1. A dice rolling simulator

import random


def roll(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled


def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling = False

    print("Thanks for playing")


main()
