import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input(
                "Invalid choice. Please choose rock, paper, or scissors: "
            ).lower()

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ")

    print("Thanks for playing!")


play_game()
