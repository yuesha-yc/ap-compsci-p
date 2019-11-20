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

def encrypt(message, key):
    # YOUR CODE HERE
    cytext = ""
    for letter in message:
        if letter == " ":
            cytext += " "
        else:
            num = ord(letter)
            cynum = num + key
            if cynum > 122:
                cynum -= 26
            cy = chr(cynum)
            cytext += cy
    return cytext

result = encrypt("gardensalad", 10)
print(result)

