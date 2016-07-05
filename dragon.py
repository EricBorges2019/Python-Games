import time; import random; import sys;
# import for later code

def longLine():
	print('-------------------------------------------------------')
def wait(delayTime):
	time.sleep(delayTime)
req_version = (3,0)
cur_version = sys.version_info

if cur_version < req_version:

	print("You are using an outdated version of Python.")
	longLine()
	wait(2)
	print("									   ")
	quit()
# check for correct version of Python

def displayIntro():
    print('You are in a land full of dragons.')
    wait(2)
    print('In front of you, there are two caves inhabited by dragons.')
    wait(2)
    print('One will share a small portion of gold with you.')
    wait(2)
    print('The other will eat you alive.')
    wait(2)
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    wait(2)
    print('It is dark and spooky...')
    wait(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    wait(2)

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

    wait(2)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
