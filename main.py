import random

def get_user_choice():
   
    while True:
        user_input = input("Choose rock, paper, or scissors : ").lower().strip()

        if user_input == "quit":
            print("Thanks for playing!")
            exit()

        if user_input in ["rock", "paper", "scissors"]:
            return user_input
   
        print("Invalid choice. Please try again")

def determine_winner(user_choice, computer_choice):
   
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def main():
   
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'quit' at any time to exit\n")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose : {user_choice}")
        print(f"Computer chose : {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            print("You win!")
            user_score += 1
        elif result == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score - You : {user_score} | Computer : {computer_score}\n")
        
        play_again = input("Play again? (y/n) : ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
