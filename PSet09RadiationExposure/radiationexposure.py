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
    gap = int((stop - start)/step)
    timeposts = [0] * gap
    n = 0
    exposure = 0
    for i in timeposts:
        i = f(start+step*n) * step
        n = n + 1
        exposure += i
    return exposure

result = decaycurvearea(5, 11, 1)
print(result)

