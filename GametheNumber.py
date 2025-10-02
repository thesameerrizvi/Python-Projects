import random

def guess_the_number():
    print("Welcome to 'Guess the Number' Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        # Take user input
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        # Check the guess
        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")

# Start the game
if __name__ == "__main__":
    guess_the_number()
