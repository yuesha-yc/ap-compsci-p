"""
|-------------------------------------------------------------------------------
| notefrequency.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 15, 2019
|
| This program determines the frequency(in Hz) for a particular octave and
| pitch class.
|
"""

def temperedscale(octave, pitch):
    # YOUR CODE HERE
    frequency = 440 * 2 ** ((octave - 4) + ((pitch - 9) / 12.0))
    return frequency

result = temperedscale(4, 6)
print(result)
