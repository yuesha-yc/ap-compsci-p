"""
|-------------------------------------------------------------------------------
| radiationexposure.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Nov 10, 2019
|
| This program determines the amount of radiation exposure.
|
"""

import math

# this function describes the radioactive decay curve of Cobalt-60
def f(x):
    activity = 10*math.e**(math.log(0.5)/5.27 * x)
    return activity

def decaycurvearea(start, stop, step):
    # YOUR CODE HERE
    radiation = 0
    i = start
    while i < stop:
        
        radiation += (f(i) * step)
        i += step
    return radiation

result = decaycurvearea(5, 11, 1)
print(result)

