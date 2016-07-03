# -*- coding: utf-8 -*-
#This program greets itself and asks for your name
import time; import random
guessesTaken = 0
#preparing some of the code for later
print('************************************************')
print('THIS PROGRAM ONLY RUNS IN PYTHON 3 AND UP')
print('USE THE "python3" COMMAND if you can to run this')
print('************************************************')
time.sleep(2.5)
print('                                          ')
print('Hello there!')
time.sleep(1)
#delay so it feigns typing
print('What is your name? (type name)')
playerName = input()
time.sleep(2)
print('Glad to meet you, ' + playerName + '!')
time.sleep(2)
print('I wanted to try a game with you.')
time.sleep(2)
number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
time.sleep(2)
guessesLeft = 6 - guessesTaken
guessesLeft = str(guessesLeft)
time.sleep(2)
print('You have ' + guessesLeft + ' guesses left.')
while guessesTaken < 6:
    print('Take a guess! (type guess)')
    guess = input()
    try:
        guess = int(guess)
    except ValueError:
        print('Oops! Only type in numbers, please!')
        continue

    guessesTaken = guessesTaken + 1


    if guess > 20:
        print('It only goes up to 20, okay?')

    if guess < 0:
        print('The number is not below 0, alright?')
#berating the player for guessing over the boundaries
    if guess < number:
        print('Too low.')



    if guess > number:        
        print ('Too high.')
        

    if guess == number:
        break
    

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + playerName + '! You guessed it in ' + guessesTaken + ' tries!')

if guess != number:
    number = str(number)
    print('Nope. The number was ' + number + '.')
    
print('GAME OVER')
