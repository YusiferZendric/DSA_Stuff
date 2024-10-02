import random

randonnum = random.randint(1,1000)
chances = 10
while True:
    guess = int(input("Enter your guess (hint: number is between 1 to 1000): "))
    if guess == randonnum:
        print(f"You won! Correct Guess: {randonnum}")
        break
    elif guess > randonnum:
        chances-=1
        print(f"your guess is bigger,try again (chances left): {chances}")
    elif guess < randonnum:
        chances-=1
        print(f"your number is smaller, try again (chances left): {chances}")
    