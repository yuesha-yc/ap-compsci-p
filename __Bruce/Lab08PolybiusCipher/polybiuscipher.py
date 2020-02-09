"""
|-------------------------------------------------------------------------------
| polybiuscipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 14, 2019
|
| This program decrypts a message using the polybius cipher.
|
"""

def decrypt(message, key):
    messageNumber = []
    for char in message:
        messageNumber.append(ord(char) - 97)

    decryptMessage = ""
    for index in range(0, len(messageNumber) - 1, 2): 
        decryptMessage += key[messageNumber[index]][messageNumber[index + 1]]
    
    return decryptMessage

#        0    1    2    3    4    5
key = [["n", "a", "1", "c", "3", "h"],
       ["8", "t", "b", "2", "o", "m"],
       ["e", "5", "w", "r", "p", "d"],
       ["4", "f", "6", "g", "7", "i"],
       ["9", "j", "0", "k", "l", "q"],
       ["s", "u", "v", "x", "y", "z"]]
message = "bcfbfeacbdadafcacafacacedfffffabfa"
result = decrypt(message, key)
print(result)

