from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt

plaintext = "dontPanic"

mykey=b"supa_key"
# key_64 = b64encode(mykey)
# print(key_64)

#mykey = b64decode(key_64)

mykey = "c3VwYV9rZXk="

ciphertext = encrypt(mykey, plaintext)
b64_representation=b64encode(ciphertext)

ciphertext = b64decode(b64_representation)
plaintext = decrypt(mykey, ciphertext)

print(plaintext)
print(b64_representation)
