"""
|-------------------------------------------------------------------------------
| eastersunday.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 10, 2019
|
| This program determines the month and day of Easter.
|
"""

def retrievedate(year):
    # Determine the month and day that Easter occurs, given a particular year.
    # YOUR CODE HERE
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    return (n, p)

result = retrievedate(2001)
print(result)
