import time; import random; import sys;
# import for later code

def longLine():
	print('_______________________________________________________')
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
		print("   ")
		quit()
# check for correct version of Python

def displayIntro():
	print('You are in a land full of dragons. In front of you,')
	print('you see two caves inhabited by dragons. One will')
	print('share a small portion of gold with you, and the')
	print('other will eat you alive.')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
	cave = input()

	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	delay(1.5)
	print('It is dark and spooky...')
	delay(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	delay(2)

		friendlyCave = random.randint(1, 2)

		if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
		else:
		print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	displayIntro()

	caveNumber = chooseCave()

	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()
