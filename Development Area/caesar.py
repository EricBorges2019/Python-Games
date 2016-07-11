# Caesar Cipher

import time; import random; import sys;
# import for later

def longLine():
    print('-------------------------------------------------------')
def wait(delayTime):
    time.sleep(delayTime)
req_version = (3,0)
cur_version = sys.version_info


def required:
    (req_version)
def available:
    (cur_version)

if cur_version < req_version:
    longLine()
    print("You are using the wrong version of Python.")
    longLine()
    print("Your interpretor is " + str(available) + " instead of at least " + str(required) + ".")
    wait(2)
    print("                                       ")
    quit()
# check for correct version of Python


MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print("Here's your translated text:")
print(getTranslatedMessage(mode, message, key))
