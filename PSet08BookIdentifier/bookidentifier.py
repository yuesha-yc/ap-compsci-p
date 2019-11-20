"""
|-------------------------------------------------------------------------------
| bookidentifier.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 28, 2019
|
| This program checks the validity of ISBN codes.
|
"""

def validatebook(isbncode):
    # YOUR CODE HERE
    n = 1
    s = 0
    isbn = isbncode[0:9]
    for i in isbn:
        s += int(i) * n
        n = n + 1
    if int(isbncode[9]) == s%11:
        result = "YES"
    else:
        result = "NO"
    return result

result = validatebook("0789751984")
print(result)

