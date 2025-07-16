'''
Write a Python program where:

The computer picks a random number between 1 and 20.

The player has 5 attempts to guess it.

After each guess:

If the guess is too low → print "Too low!"

If the guess is too high → print "Too high!"

If the guess is correct → print "Congratulations, you guessed it!" and end the game.

If the player uses all 5 attempts without guessing → print "Sorry, you lost! The number was X."

'''
import random
random_num = random.randint(1, 20)
attempt_count = 0

while(attempt_count<5):
    user_guess=int(input(f"Enter Your Guess -: "))
    if user_guess == random_num:
        print(f"Hoooray..!! Your Guess was Correct!")
    elif user_guess < random_num:
        print("Too Low...!")
    elif user_guess > random_num:
        print("Too High...!")
    if attempt_count == 5:
        print("You used your 5 guesses")
    else:
        attempt_count = attempt_count +1

print("The actual number was -: ", random_num)