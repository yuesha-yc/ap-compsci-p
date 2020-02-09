"""
|-------------------------------------------------------------------------------
| vigenerecipher.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 22, 2019
|
| This program encrypts a message with the vigenere cipher.
|
"""

import math

def ch2ord(ch):
    return ord(ch) - 97

def ord2ch(o):
    return chr(o + 97)

def encrypt(message, key):
    # YOUR CODE HERE
    i = 0
    ans = ""
    keylen = len(key)
    for char in message:
        #print(char + "+" + key[i])
        char = ord2ch((ch2ord(char) + ch2ord(key[i])) % 26)
        #print("=" + char)
        ans += char
        i += 1
        if i == keylen: i = 0
        #print(ans)
        #print("")
        
    return ans

result = encrypt("meetmeattheparkatelevenam", "bacon")
print(result)
# neghzfavhufpcfxbtgzrwepoz
# negzfavufpcxbtgzrwepoz
# neg zfav ufpc xbtgzrwepoz
