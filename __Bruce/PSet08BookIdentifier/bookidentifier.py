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
    i = 1
    verify = 0
    for char in isbncode:
        verify += (i * int(char))
        i += 1
        if i == 11: break
        
    verify = verify % 11
    if verify == int(isbncode[9]): return "YES"
    else: return "NO"
result = validatebook("0789751984")
print(result)

