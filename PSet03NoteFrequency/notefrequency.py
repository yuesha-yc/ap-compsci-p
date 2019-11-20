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
    octa = octave - 4
    semi = pitch - 9
    ref = 440
    frequency = ref * 2 ** (octa + (semi / 12.0))
    return frequency

result = temperedscale(0, 0)
print(result)
