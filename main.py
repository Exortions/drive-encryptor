E=exit
import drive_decryptor as C,drive_encryptor as D
def A():
	print('1. Encrypt a drive\n2. Decrypt a drive\n3. Exit');B=input('\nEnter your choice: ')
	if B=='1':D.run();A()
	elif B=='2':C.run();A()
	else:E(0)
	E(0)
if __name__=='__main__':A()