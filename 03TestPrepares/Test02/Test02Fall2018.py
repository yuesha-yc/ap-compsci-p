# Part III, Problem 1

def inventory():
    #”””
    #returns a float, the total value of all the products.
    #”””
    prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
    stock = {"banana":6, "apple":7, "orange":31, "pear":15}
    # YOUR CODE HERE
    total = 0
    price = list(prices.values())
    quantity = list(stock.values())
    for i in range(0,len(price)):
        total += price[i] * quantity[i]
    return total

result = inventory()
print(result)