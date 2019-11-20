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
    # Transform the letters in the message into string of integers
    number = ""
    for letter in message:
         if letter == "a":
             number += "0"
         elif letter == "b":
             number += "1"
         elif letter == "c":
             number += "2"
         elif letter == "d":
             number += "3"
         elif letter == "e":
             number += "4"
         elif letter == "f":
             number += "5"

    # Divide the string of integer into two strings of the row and column
    n = 0
    rownum = ""
    columnnum = ""
    for num in number:
        if n%2 == 0:
            rownum += num
        else:
            columnnum += num
        n += 1

    # Loop across the row and column strings to get the final message
    final = ""
    for i in range(0,len(rownum)):
        value = key[int(rownum[i])][int(columnnum[i])]
        final += value

    return final

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

