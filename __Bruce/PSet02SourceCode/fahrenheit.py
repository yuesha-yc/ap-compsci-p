"""
|-------------------------------------------------------------------------------
| fahrenheit
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Aug 14, 2019
|
| This program converts celsius to fahrenheit.
|
"""

def calculatefahrenheit(celsius):
    # Use the provided equation to convert celsius to fahrenheit.
    # YOUR CODE HERE
    celsius = celsius * 9
    celsius = celsius / 5
    return celsius + 32
result = calculatefahrenheit(100)
print(result)

