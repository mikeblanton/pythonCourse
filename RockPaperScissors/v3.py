from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(Enter your choice): ").lower()
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
    elif computer == "scissors":
        print("You win!")
elif player1 == "paper":
    if computer == "scissors":
        print("Computer wins!")
    elif computer == "rock":
        print("You win!")
elif player1 == "scissors":
    if (computer == "rock"):
        print("Computer wins!")
    elif computer == "paper":
        print("You win!")
else:
    print("Something went wrong!")
