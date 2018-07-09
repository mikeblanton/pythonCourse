from random import randint

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player1 = input("(Enter your choice): ").lower()
    if player1 == "quit":
        break

    computer = randint(0, 2)
    if computer == 0:
        computer = "rock"
    elif computer == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}")

    if player1 == computer:
        print("It's a tie!")
    elif player1 == "rock":
        if computer == "paper":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "scissors":
            print("You win!")
            player_wins += 1
    elif player1 == "paper":
        if computer == "scissors":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "rock":
            print("You win!")
            player_wins += 1
    elif player1 == "scissors":
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("You win!")
            player_wins += 1
    else:
        print("Something went wrong!")

if player_wins > computer_wins:
    print("You win!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("The computer won!")
