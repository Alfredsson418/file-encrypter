# https://cryptography.io/en/latest/
# https://realpython.com/python-command-line-arguments/#the-command-line-interface
from cryptography.fernet import Fernet
import sys
args = sys.argv
if len(args) < 3:
    sys.exit("Missing Arguments!")

encryptDir = args[1]
keyDir = args[2]


key = Fernet.generate_key()

# Sparar Nyckeln
with open(keyDir + "key.txt", "wb") as keyFile:
    keyFile.write(key)

f = Fernet(key)

# Läser Filen och sparar innehållet som binärt 
with open(encryptDir, "rb") as file:
    token = f.encrypt(file.read())

# Skriver över innehållet som binärt
with open(encryptDir, "wb") as file:
    file.write(token)