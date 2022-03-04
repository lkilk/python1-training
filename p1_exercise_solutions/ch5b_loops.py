import random

magic_number = random.randint(1, 10)
for i in range(3):
    user_guess = input("Guess the magic number between 1 and 10: ")
    user_guess = int(user_guess)
    if user_guess == magic_number:
        print("Winner!")
        break
    elif user_guess < magic_number:
        print("Too low")
    elif user_guess > magic_number:
        print("Too high")
else:
    print("Loser!")