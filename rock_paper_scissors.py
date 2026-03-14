import random

# Global scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]


def display_title():
    print("\n==============================")
    print(" ROCK PAPER SCISSORS GAME ")
    print("==============================")


def get_user_choice():
    user = input("\nEnter rock, paper, scissors (or exit): ").lower()

    if user == "exit":
        return None

    if user not in choices:
        print("⚠ Invalid choice. Try again.")
        return get_user_choice()

    return user


def get_computer_choice():
    return random.choice(choices)


def decide_winner(user, computer):
    global user_score, computer_score

    if user == computer:
        print("🤝 It's a Tie")

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):

        print("🎉 You Win")
        user_score += 1

    else:
        print("😢 Computer Wins")
        computer_score += 1


def show_choices(user, computer):
    print("\nYou chose:", user)
    print("Computer chose:", computer)


def show_score():
    print("\n📊 SCORE")
    print("You:", user_score)
    print("Computer:", computer_score)


def play_again():
    again = input("\nPlay again? (yes/no): ").lower()
    return again == "yes"


def main():
    display_title()

    while True:
        user = get_user_choice()

        if user is None:
            break

        computer = get_computer_choice()

        show_choices(user, computer)
        decide_winner(user, computer)
        show_score()

        if not play_again():
            break

    print("\n✅ Final Score")
    show_score()
    print("Game Over")


if __name__ == "__main__":
    main()