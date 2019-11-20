"""
|-------------------------------------------------------------------------------
| smoothsignal.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Oct 30, 2019
|
| This program smoothes an audio signal by averaging intensities.
|
"""

def levelling(audio):
    # YOUR CODE HERE
    smooth = [0] * len(audio)
    smooth[0] = (audio[0]+audio[1])//2
    smooth[-1] = (audio[-2]+audio[-1])//2
    for i in range(1,len(audio)-1):
        smooth[i] = (audio[i-1] + audio[i] + audio[i+1])//3

    return smooth

signal = [1, 5, 4, 5, 7, 6, 8, 6, 5, 4, 5, 4]
result = levelling(signal)
print(result)

