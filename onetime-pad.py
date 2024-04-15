import random

plaintext = "The Quick Brown Fox Jumps Over The Lazy Dog"

def cleantext(message):

    message = ''.join(c for c in message if c.isalnum())
    # Convert all characters to lowercase
    message = message.lower()
    # Remove all spaces
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

decrypted = decrypt(encrypted, key)

print("Decrypted Message: " + decrypted)