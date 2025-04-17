import random

# Randomly select a number between 1 and 20
secret_number = random.randint(1, 20)

# Set a limit for the number of attempts
attempts = 0
max_attempts = 5

# Game loop
while attempts < max_attempts:
    # Ask the user for a guess
    guess = int(input("Guess the number (between 1 and 20): "))

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break  # Stop the game if the correct number is guessed

    if attempts == max_attempts:
        print(f"Game over! The correct number was {secret_number}.")