import random

def numbergame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = (int(input("Make a guess: ")))
            attempts += 1
            
            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")