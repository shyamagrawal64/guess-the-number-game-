import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    secret_num = random.randint(1, 100)

    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess == secret_num:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_num:
            print("Try again. Go higher.")
        else:
            print("Try again. Go lower.")


guess_the_number()