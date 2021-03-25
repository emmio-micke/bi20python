import random

# Slumpa fram ett ord
words = ["apple", "orange", "kiwi", "strawberry"]
random_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0

while True:
    # Skriv ut vår gissa-sträng - - - - - -
    random_word_user = ""
    for letter in random_word:
        if letter in guessed_letters:
            random_word_user += letter
        else:
            random_word_user += "_"

    if random_word == random_word_user:
        print("Du har gissat rätt ord! " + random_word)
        break

    print("----------")
    print("Ordet vi letar efter: " + random_word_user)
    print("Dina gissningar: " + str(guessed_letters))
    print("Antalet felgissningar: " + str(wrong_guesses))

    # Läs in en bokstav från användaren
    user_letter = input("Gissa en bokstav: ")
    guessed_letters.append(user_letter)

    # Finns bokstaven i vårt ord?
    if user_letter in random_word:
        print("Bra, den bokstaven finns med!")
    else:
        print("Synd, den bokstaven finns inte med!")
        wrong_guesses += 1

    if wrong_guesses >= 10:
        print("Game over!")
        break
