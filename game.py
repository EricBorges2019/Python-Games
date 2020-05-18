import time; import sys;
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
