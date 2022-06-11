# https://cryptography.io/en/latest/
from cryptography.fernet import Fernet
import sys, os

args = sys.argv
if len(args) < 3:
    sys.exit("Missing Arguments!")

encryptDir = args[1]
keyDir = args[2]

# Generates and saves key
key = Fernet.generate_key()
with open(keyDir + "/key.txt", "wb") as keyFile:
    keyFile.write(key)
f = Fernet(key)

def encrypt(encryptFilePath):

    # Reads files and creates encrypted material
    with open(encryptFilePath, "rb") as file:
        material = f.encrypt(file.read())

    # Overwrites file with encrypted material
    with open(encryptFilePath, "wb") as file:
        file.write(material)

if os.path.isfile(encryptDir):
    encrypt(encryptDir)
else:

    for path, subdirs, files in os.walk(encryptDir):
        for name in files:
            encrypt(os.path.join(path, name))

