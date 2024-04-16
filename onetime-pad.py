import random

plaintext = input("Enter some text to encrypt: ")

def cleantext(message):

    message = ''.join(c for c in message if c.isalnum())

    message = message.lower()

    message = ''.join(message)
    return message

text = cleantext(plaintext)

def generatekey(message):

    key = ""

    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in range(0, len(message)):
        key = key + random.choice(alphabet)

    return key

key = generatekey(text)

print("Key: " + key)

def encrypt(message, key):

    encrypted = ""

    for character, letter in zip(message, key):

        joined = ord(character) + ord(letter)
        
        encrypted = encrypted + chr(joined)
        
    return encrypted

encrypted = encrypt(text, key)

print("Encrypted Message: " + encrypted)

def decrypt(encryptedtext, key):
    
    decrypted = ""
    
    for character, letter in zip(encryptedtext, key):

        joined = ord(character) - ord(letter)
        
        decrypted = decrypted + chr(joined)
        
    return decrypted

encryptText = input("Enter encrypted text: ")
keyText = input("Enter key: ")

decrypted = decrypt(encryptText, keyText)

print("Decrypted Message: " + decrypted)