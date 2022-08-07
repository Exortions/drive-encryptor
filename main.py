import drive_decryptor
import drive_encryptor

if __name__ == '__main__':
	print('1. Encrypt a drive\n2. Decrypt a drive\n3. Exit')
	choice = input('\nEnter your choice: ')

	if choice == '1':
		drive_encryptor.run()
	elif choice == '2':
		drive_decryptor.run()
	else:
		exit(0)