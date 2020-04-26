import random
import sys


class Error (Exception):
    pass


class InputError (Error):
    pass

class InputError2 (Error):
    pass


lower_limit = 1
upper_limit = 0
iteration = 0
level_display = ""


def define_level(choice):
    global upper_limit
    global iteration
    global level_display

    if choice == "1":
        upper_limit = 10
        iteration = 6
        level_display = "Easy"

    if choice == "2":
        upper_limit = 20
        iteration = 4
        level_display = "Medium"

    if choice == "3":
        upper_limit = 50
        iteration = 3
        level_display = "Hard"


print("This is a Number Guessing game.")

while True:
    while True:
        try:
            level = input("Choose level: 1 - Easy || 2 - Medium || 3 - Hard > ")
            if level != "1" and level != "2" and level != "3":
                raise InputError
            break
        except InputError:
            print("Please enter 1, 2 or 3")

    define_level(level)

    number = random.randint(lower_limit, upper_limit)

    guessed_number = None

    '''You can remove the hashtag in the line below for testing purposes'''
    #print(number)

    print(f"A number between {lower_limit} and {upper_limit} has been chosen at random for you to guess.\nThis is the {level_display} level and you have {iteration} guesses.")

    while iteration > 0:
        try:
            guessed_number = int(input("Guess the number > "))

            iteration -= 1

            if guessed_number == number:
                print(f"You got it right! The number is {number}. YOU WON!")
                break
            else:
                if iteration > 0:
                    print(f"That was wrong. You have {iteration} more guess(es).")
                else:
                    print(f"You have no more guesses")
        except ValueError:
            print("Please enter a number")

    if iteration == 0 and guessed_number != number:
        print(f"The number was {number}. GAME OVER!")

    while True:
        try:
            new_game = input("Do you want to play again? Yes (Y) || No (N)")

            if new_game == "Y" or new_game == "y":
                print("")
                break
            elif new_game == "N" or new_game == "n":
                sys.exit("Good bye!")
            else:
                raise InputError2
        except InputError2:
            print('Please enter "Y" or "N"')

