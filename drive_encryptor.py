import random
import string
import time
import os

from cryptography.fernet import Fernet
from ctypes import windll

def get_drives() -> list:
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()

    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    
    return drives

def generate_encryption_key() -> bytes:
    return Fernet.generate_key()


def run():
    drives = get_drives()

    maxlen = len('vailable drives ')

    print('-' * (maxlen + 4))
    print('| Available drives |')
    print('| ' + ('-' * (maxlen)) + ' |')

    for drive in drives:
        print('| {}'.format(drive) + (' ' * maxlen) + '|')

    print('-' * (maxlen + 4))

    drive = input('\nEnter drive to encrypt: ').upper()
    print('\n')

    if drive not in drives:
        print('Invalid drive')
        exit(1)

    drive = drive.upper() + ':\\'

    print(f'Encrypting drive {drive}...\n')

    files = []
    for (dir_path, dir_names, file_names) in os.walk(drive):
        files.extend(f'{dir_path}\\{file_name}' for file_name in file_names)

    print(f'About to encrypt {len(files)} file{"s" if len(files) != 1 else ""}...')
    print('Press enter to continue, or press anything and enter to cancel')

    should_cancel = input()

    if should_cancel != '':
        print('Aborting...')
        exit(0)

    encryption_key = generate_encryption_key()

    fancy_key = str(encryption_key)[2:-1]

    print(f'Encrypting with key: {fancy_key}')

    fname = time.asctime().replace(' ', '_').replace(':', '_') + '.key.txt'

    print(f'Saving key to {fname}...')
    open(fname, 'wb').write(encryption_key)
    print(f'Successfully saved key to {fname}\n')

    files = list(files)

    for file in files:
        files[files.index(file)] = file.replace(drive + '\\', drive)

    for file in files:
        print(f'Encrypting {file}...')

        with open(file, 'rb') as f:
            data = f.read()
        
        fernet = Fernet(encryption_key)
        encrypted_data = fernet.encrypt(data)

        with open(file, 'wb') as f:
            f.write(encrypted_data)

        print(f'Successfully encrypted {file} ({data})\n')

    print(f'\nSuccessfully encrypted {len(files)} file{"s" if len(files) != 1 else ""}')
    print('Press enter to exit')
    input()