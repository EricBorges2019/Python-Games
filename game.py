import time; import random; import sys;
# import for later code

def longLine():
	print('-------------------------------------------------------')
def wait(delayTime):
	time.sleep(delayTime)
req_version = (3,0)
cur_version = sys.version_info

if cur_version < req_version:

	print('You are using an unsupported version of Python.')
	longLine()
	wait(2)

	print('Type help() into your interpreter.')
	longLine()
	wait(2)

	print('If a version before 2.7 appears, then install Python 3.')
	longLine()
	wait(2)

	print('Use the Python launcher which comes with Python 3.')
	longLine()
	wait(2)

	print('Use the python3 command on macOS (OS X)')
	wait(2)
	print("									   ")
	quit()
# check for correct version of Python

guessesTaken = 0
wait(2)

print('										  ')
print('Hello there!')
wait(1)
#delay

print('What is your name? (type name)')
playerName = input()
wait(2)

print('Glad to meet you, ' + playerName + '!')
wait(2)

number = random.randint(2, 19)
print('I am thinking of a number between 1 and 20.')
wait(2)

guessesLeft = 6 - guessesTaken
guessesLeft = str(guessesLeft)
wait(2)

print('You have ' + guessesLeft + ' guesses left.')
wait(2)

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
		print("You're supposed to guess between 1 and 20, silly!")

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
