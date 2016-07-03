# -*- coding: utf-8 -*-
#This program greets itself and asks for your name
import time; import random; import sys

req_version = (3,0)
cur_version = sys.version_info

if cur_version < req_version:
    print('You are using an unsupported version of Python. Please run this with Python 3.')

guessesTaken = 0
#preparing some of the code for later
time.sleep(2.5)
print('                                          ')
print('Hello there!')
time.sleep(1)
#delay
print('What is your name? (type name)')
playerName = input()
time.sleep(2)
print('Glad to meet you, ' + playerName + '!')
time.sleep(2)
number = random.randint(2, 19)
print('I am thinking of a number between 1 and 20.')
time.sleep(2)
guessesLeft = 6 - guessesTaken
guessesLeft = str(guessesLeft)
time.sleep(2)
print('You have ' + guessesLeft + ' guesses left.')
time.sleep(2)
while guessesTaken < 6:
    print('Type in your guess!')
    guess = input()
    try:
        guess = int(guess)
    except ValueError:
        print('Oops! Only type in numbers, please!')
        continue
#Berating the player for not typing in a number
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
#feedback for the player

    if guess == number:
        break
#break the feedback loop and start the "YOU WON text"

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + playerName + '! You found it in ' + guessesTaken + ' tries!')

if guess != number:
    number = str(number)
    print('Sorry! The number was ' + number + '.')

print('Thanks for playing!')

print('GAME OVER')
