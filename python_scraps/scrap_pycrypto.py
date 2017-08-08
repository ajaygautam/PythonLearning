from base64 import b64encode, b64decode
from Crypto.Cipher import AES

plain_text = "dontPanic"
mykey="This is a key123"
app_name = "CashManagement"


# Encryption
encryption_suite = AES.new(mykey)
cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")
b64_representation=b64encode(cipher_text)


# Decryption
cipher_text = b64decode(b64_representation)
decryption_suite = AES.new(mykey)
plain_text = decryption_suite.decrypt(cipher_text)

print(plain_text)
print(b64_representation)
