"""
|-------------------------------------------------------------------------------
| vigenerecipher.py
|-------------------------------------------------------------------------------
|
| Author:  Kevin Wang Yichen
| Created: Nov 22, 2019
|
| This program encrypts a message with the vigenere cipher.
|
"""

def encrypt(message, key):
    # YOUR CODE HERE
    cytext = ""
    for i in range(0,len(message)):
        cynum = ord(message[i]) + ord(key[i%len(key)]) - 97
        if cynum > 122:
            cynum -= 26
        cytext += chr(cynum)
    return cytext

result = encrypt("hello", "abc")
print(result)

