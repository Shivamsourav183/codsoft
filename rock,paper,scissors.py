import random

def get_computer_choice(options):
    return random.choice(options)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You won!"
    else:
        return "You lost!"

def display_score(user_wins, computer_wins):
    print(f"\nScore: You {user_wins} - {computer_wins} Computer\n")

def play_game():
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("==========================================\n")
    
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user == "q":
            break
        if user not in options:
            print("Invalid choice. Please try again.")
            continue

        computer = get_computer_choice(options)
        print(f"Computer choice: {computer}")

        result = determine_winner(user, computer)
        print(result)
        
        if result == "You won!":
            user_wins += 1
        elif result == "You lost!":
            computer_wins += 1

        display_score(user_wins, computer_wins)
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"\nFinal Score: You {user_wins} - {computer_wins} Computer")
    print("Goodbye!")

if __name__ == "__main__":
    play_game()
