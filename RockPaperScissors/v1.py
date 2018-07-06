print("...rock...")
print("...paper...")
print("...scissors...")

p1_choice = input("(enter Player 1's choice): ")
p2_choice = input("(enter Player 2's choice): ")

print("SHOOT!")

if p1_choice == "rock" and p2_choice == "scissors":
    print("Player 1 wins!")
elif p1_choice == "paper" and p2_choice == "rock":
    print("Player 1 wins!")
elif p1_choice == "scissors" and p2_choice == "paper":
    print("Player 1 wins!")
elif p2_choice == "rock" and p1_choice == "scissors":
    print("Player 2 wins!")
elif p2_choice == "paper" and p1_choice == "rock":
    print("Player 2 wins!")
elif p2_choice == "scissors" and p1_choice == "paper":
    print("Player 2 wins!")
else:
    print("Draw!")
