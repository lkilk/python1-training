import random 
magic_number = random.randint(1, 10)

loopcnt = 0 

#while loopcnt < 3:
#    user_guess = int ( input("Guess the Magic Number between 1 and 10: ") )
#    loopcnt += 1
#    if user_guess == magic_number:
#        print("Winner!")
#        break
#    elif user_guess < magic_number:
#        print("Too Low")
#    elif user_guess > magic_number:
#        print("Too High")
#else:
#   print("Out of guesses, better luck next time!")

for i in range(3):
    user_guess = int ( input("Guess the Magic Number between 1 and 10: ") )
    if user_guess == magic_number:
        print("Winner!")
        break
    elif user_guess < magic_number:
        print("Too Low")
    elif user_guess > magic_number:
        print("Too High")
else:
    print("Out of guesses, better luck next time!")