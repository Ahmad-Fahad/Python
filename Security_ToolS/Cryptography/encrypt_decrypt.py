from cryptography.fernet import Fernet

'''
key = Fernet.generate_key()
with open('key.txt', 'wb') as f:
	f.write(key)

'''

def encryption(msg):
	with open('key.txt', 'rb') as f:
		key = f.read()
		fernet = Fernet(key)
		encrypted_data = fernet.encrypt(msg)
		print(encrypted_data)
	with open('cipher.txt', 'wb') as f:
		f.write(encrypted_data)


def decryption(key, cipher):
	fernet = Fernet(key)
	decrypted_data = fernet.decrypt(cipher)
	print(decrypted_data)
	with open('decrypted.txt', 'wb') as f:
		f.write(decrypted_data)

# msg encrypt
#encryption(b"I love you")
#image.jpg
# file  encrypt
with open('image.jpg', 'rb') as f:
	image_data = f.read()

encryption(image_data)

#file encrypt

print("\n")
with open('key.txt', 'rb') as f:
	key = f.read()
with open('cipher.txt', 'rb') as f:
	cipher = f.read()
decryption(key, cipher)