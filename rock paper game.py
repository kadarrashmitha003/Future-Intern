import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        # User's choice
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to stop playing): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing! 👋")
            break

        if user_choice not in choices:
            print("Invalid choice, try again!")
            continue
        
        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie! 🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win! 🎉")
        else:
            print("Computer wins! 🤖")

# Let's play!
rock_paper_scissors()
