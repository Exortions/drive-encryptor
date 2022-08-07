import string
import os

from cryptography.fernet import Fernet
from util import select_drive

def run():
    drive = select_drive()

    print(f'Decrypting drive {drive}...\n')

    files = []
    for (dir_path, dir_names, file_names) in os.walk(drive):
        files.extend(f'{dir_path}\\{file_name}' for file_name in file_names)

    print(f'About to decrypt {len(files)} file{"s" if len(files) != 1 else ""}...')
    print('Press enter to continue, or press anything and enter to cancel')

    should_cancel = input()

    if should_cancel != '':
        print('Aborting...')
        exit(0)

    key = input('Enter decryption key: ')

    files = list(files)

    for file in files:
        files[files.index(file)] = file.replace(drive + '\\', drive)

    for file in files:
        print(f'Decrypting {file}...')
        with open(file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open(file, 'wb') as f:
            f.write(decrypted)

        print(f'Successfully decrypted {file} ({data})\n')

    print(f'\nSuccessfully decrypted {len(files)} file{"s" if len(files) != 1 else ""}')
    print('Press enter to exit')
    input()