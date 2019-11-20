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
    # YOUR CODE HERE
    dict = {"a":0 ,"b":1 ,"c":2, "d":3, "e":4, "f":5}
    wyc = ""
    for i in range(0,len(message)):
        if i % 2 == 0:
            row = dict[message[i]]
        else:
            column = dict[message[i]]
            wyc += key[row][column]
    return wyc

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

