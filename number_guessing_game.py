import random

number = random.randint(1, 10)
attempts = 0

print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
