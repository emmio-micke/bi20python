from random import randint

guess_number = randint(0, 100)

continue_game = True

while continue_game:
    answer = int(input("Gissa nummer: "))

    if answer < guess_number:
        print("Du gissade för lågt!")

    if answer > guess_number:
        print("Du gissade för högt!")

    if answer == guess_number:
        print("Du gissade rätt!")
        continue_game = False

print("Spelet är slut!")
