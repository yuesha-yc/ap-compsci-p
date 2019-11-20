"""
|-------------------------------------------------------------------------------
| coinchange.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 11, 2019
|
| This program determines the the minimum number of coins for a particular value.
|
"""

def minimumcoins(cents):
    # YOUR CODE HERE
    num = cents//25 + (cents%25)//10 + ((cents%25)%10)//5 + (((cents%25)%10)%5)//1
    return num
result = minimumcoins(41)
print(result)
