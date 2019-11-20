"""
|-------------------------------------------------------------------------------
| moviecritic.py
|-------------------------------------------------------------------------------
|
| Author:  Alwin Tareen
| Created: Sep 19, 2019
|
| This program determines a user's particular interest in a certain movie.
|
"""

def selectfilm(price, rating):
    # YOUR CODE HERE
    if price >=0 and 0 <= rating <= 5:
        if price < 5 and rating >= 2:
            outcome = 'extremely interested'
        elif price >= 12:
            if rating == 5:
                outcome = 'barely interested'
            else:
                outcome = 'completely uninterested'
        elif price < 12 and rating > 4:
            outcome = 'very interested'
        elif 5 <= price <= 11.99 and 2 <= rating <= 4:
            outcome = 'moderately interested'
        elif price < 5 and rating < 2:
            outcome = 'barely interested'
        else:
            outcome = 'completely uninterested'
    else:
        outcome = 'completely uninterested'
    return outcome

result = selectfilm(6.50, 3.5)
print(result)

