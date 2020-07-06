# Guess the number game
import random

print('What is your name?')
name = input()

print('Well ' + name + ' I am thinking in a number between 1 and 20, you need to guess the number in 5 tries!')
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 5) :
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber :
        print('Your guess is too low')
    elif guess > secretNumber :
        print('Your guess is too high')
    else :
        break # Right guess

if guess == secretNumber :
    print('Good job ' + name + '! You guess the number in ' + str(guessTaken) + ' guesses.')
else :
    print('Nope, the number I wass thinking of was ' + str(secretNumber) + '. Try again')