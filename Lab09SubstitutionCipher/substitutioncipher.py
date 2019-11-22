"""
|-------------------------------------------------------------------------------
| substitutioncipher.py
|-------------------------------------------------------------------------------
|
| Author:  Kevin WYC
| Created: Nov 21, 2019
|
| This program encrypts a message using the substitution cipher.
|
"""

def encrypt(message, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # YOUR CODE HERE
    emerson = {} # 创建字典
    for i in range(0,len(alpha)): # 循环0到25
        emerson[alpha[i]] = key[i] # 每次循环把alpha里的第i位字母对应到key里的第i位字母然后加到字典里
    aynah = "" # 创建字符串
    for j in message: # 循环message里的字母
        aynah += emerson[j] # 每次把字母放到字典里读取value，加到字符串里
    return aynah #返回


result = encrypt("hello", "jtrekyavogdxpsncuizlfbmwhq")
print(result)

