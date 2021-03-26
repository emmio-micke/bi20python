from random import randint

guess_number = randint(0, 100)

continue_game = True
guesses = 0

while continue_game:
    answer = int(input("Gissa nummer: "))
    guesses += 1

    if answer < guess_number:
        print("Du gissade för lågt!")

    if answer > guess_number:
        print("Du gissade för högt!")

    if answer == guess_number:
        print(f"Du gissade rätt! Du behövde {guesses} gissningar.")
        continue_game = False

print("Spelet är slut! Du vann!")
