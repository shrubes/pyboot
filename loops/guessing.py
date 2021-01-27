from random import randint

number = randint(1, 10)
guess = int

while number != guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low, try again")
    elif guess > number:
        print("Too high, try again")
    else:
        print(f"You guessed it, the number was {number}")
        keep_playing = input("Do you want to keep playing?  (y/n) ")
        if keep_playing == "y":
            number = randint(1, 10)
            guess = None
        else:
            print("Thanks for playing!")
            break
