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
    if price < 5 and rating >= 2:
        outcome = "extremely interested"
    
    elif price >= 12:
        if rating == 5:
            outcome = "barely interested"
        else:
            outcome = "completely uninterested"
        
    elif price < 12 and rating > 4:
        outcome = "very interested"

    elif price >= 5 and price <= 11.99 and rating >= 2 and rating <= 4:
        outcome = "moderately interested"
    
    elif rating < 2:
        outcome = "barely interested"

    else:
        outcome = "completely uninterested"

    return outcome


result = selectfilm(10, 4.5)
print(result)

