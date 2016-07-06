import time; import sys;
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
		print("   ")
		quit()
# check for correct version of Python
print("What do you get when you cross a snowman with a vampire?")
input()
print("Frostbite!")
print()
print("Knock Knock!")
wait(1.5)
print("Who's there?")
wait(1.5)
print("Interrupting cow.")
wait(1.5)
print("Interrupting cow wh", end='')
wait(1)
print("-Moo!")
