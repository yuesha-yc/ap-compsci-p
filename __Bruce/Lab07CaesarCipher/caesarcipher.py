"""
|-------------------------------------------------------------------------------
| caesarcipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 06, 2019
|
| This program encrypts a message using the caesar cipher.
|
"""
def Ckey(ori):
    return ori

def encrypt(message, key):
    # YOUR CODE HERE
    result = ""
    for char in message:
        if char == " ":
            result += " "
        else:
            result += (chr(((ord(char) - 97 + key) % 26) + 97))
    return result

result = encrypt("gardensalad", 10)
print(result)

