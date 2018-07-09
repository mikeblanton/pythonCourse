import random

play = "y"

while play == "y":
    guess = 0
    number = random.randint(1, 10)
    while guess != number:
        guess = int(input("Pick a number between 1 and 10: "))
        if guess < number:
            print("You're too low!")
        elif guess > number:
            print("You're too high!")

    print("You guessed it!")
    play = input("Would you like to play again? (y/n) ")

print("Thanks for playing!")
