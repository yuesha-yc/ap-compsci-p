
#14
def circlearea(radius):
    #variable radius formal name: parameter
    return radius
#15 valid string methods
#16 string add
#17 string slice: start with 0

#questin 34
x = 25
y = 5
while y <= x:
    y = y + 5

#Question 35
def countvowels(sample):
    count = 0
    for letter in sample:
        if letter in "aeiou":
            count += 1
    return count

#Question 36
def extraend(word):
    last = word[-2:]
    result = 3*last
    return result

# Question 37 Piglatin
def piglatin(english):
    if english[0] in "aeiou":
        pig = english + "hay"
    else:
        pig = english[1:] + english[0] + "ay"
    return pig

result = piglatin("peach")
print(result)

# Question 38 Coder
def caesarcipher(plaintext, shift):
    cytext = ""
    for letter in plaintext:
        p_num = ord(letter)
        c_num = (p_num + shift)
        while c_num > 122:
            c_num = c_num - 26
        c = chr(c_num)
        cytext += c
    return cytext

result = caesarcipher("mayday", 4)
print(result)

# Question 38 Decoder
def caesarcipher_decoder(cytext, shift):
    plaintext = ""
    for letter in cytext:
        cnum = ord(letter)
        pnum = cnum - shift
        while pnum < 97:
            pnum = pnum + 26
        p = chr(pnum)
        plaintext += p
    return plaintext

result = caesarcipher_decoder("qechec", 4)
print(result)



