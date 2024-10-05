import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    guess = None
    hint_given = False
    
    while guess != number_to_guess:
        try:
            # Ask the user to guess the number
            guess = int(input("Enter your guess: "))
            
            # Increase the attempt count
            attempts += 1
            
            # Provide hints
            if guess < number_to_guess:
                if not hint_given:
                    print("Hint 1: The number is higher.")
                    hint_given = True
                elif abs(guess - number_to_guess) <= 10:
                    print("Hint 2: You're very close! The number is slightly higher.")
                else:
                    print("Hint 2: The number is much higher.")
                    
            elif guess > number_to_guess:
                if not hint_given:
                    print("Hint 1: The number is lower.")
                    hint_given = True
                elif abs(guess - number_to_guess) <= 10:
                    print("Hint 2: You're very close! The number is slightly lower.")
                else:
                    print("Hint 2: The number is much lower.")
                    
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                return
        
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()
