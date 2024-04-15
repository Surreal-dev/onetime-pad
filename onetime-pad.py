import random

plaintext = "This is an ENCRYPTED message!"

def cleantext(message):

    clean = ""

    for letter in message:
        if letter.isalpha():
            clean = clean + letter

    return clean

def generatekey(message):

    key = ""

    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    text = cleantext(message)

    for letter in range(0, len(text)):
        key = key + random.choice(alphabet)

    return key

key = generatekey(plaintext)

print(key)

def encrypt(message, key):

    encrypted = ""

    for character, letter in message, key:

        encrypted = encrypted + char(ord(character) + ord(letter))