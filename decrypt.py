from cryptography.fernet import Fernet
import sys, os

args = sys.argv
if len(args) < 3:
    sys.exit("Missing Arguments!")

decryptDir = args[1]
keyDir = args[2]

# Finds and saves key
with open(keyDir, "rb") as keyFile:
    key = keyFile.read()
f = Fernet(key)

def decrypt(decryptFilePath):

    # Reads files and creates decrypted material
    with open(decryptFilePath, "rb") as file:
        material = f.decrypt(file.read())

    # Overwrites file with decrypted material
    with open(decryptFilePath, "wb") as file:
        file.write(material)

if os.path.isfile(decryptDir):
    decrypt(decryptDir)
else:

    for path, subdirs, files in os.walk(decryptDir):
        for name in files:
            decrypt(os.path.join(path, name))
