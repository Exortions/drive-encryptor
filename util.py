import string

from ctypes import windll

def get_drives() -> list:
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()

    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    
    return drives

def select_drive() -> str:
    drives = get_drives()

    maxlen = len('vailable drives ')

    print('-' * (maxlen + 4))
    print('| Available drives |')
    print('| ' + ('-' * (maxlen)) + ' |')

    for drive in drives:
        print('| {}'.format(drive) + (' ' * maxlen) + '|')

    print('-' * (maxlen + 4))

    drive = input('\nEnter drive to decrypt: ').upper()
    print('\n')

    if drive not in drives:
        print('Invalid drive')
        exit(1)

    drive = drive.upper() + ':\\'

    return drive