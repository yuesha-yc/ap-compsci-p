# Part III, Problem 1

def inventory():
    #”””
    #returns a float, the total value of all the products.
    #”””
    prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
    stock = {"banana":6, "apple":7, "orange":31, "pear":15}
    # YOUR CODE HERE
    total = 0
    t = 0
    price = list(prices.values())
    quantity = list(stock.values())
    for i in range(0,len(price)):
        total += price[i] * quantity[i]
    for item in prices and stock:
        t += prices[item]*stock[item]
    return t

result = inventory()
print(result)

# Problem II, DNA to RNA Transcription

def transcription(dna):
    mapping = {"A":"U", "C":"G", "G":"C", "T":"A"}
    rna = ""
    for i in dna:
        rna += mapping[i]
    return rna

result = transcription("AGGCTACGT")
print(result)

# Problem III, Numbers in Mandarin

def convert_to_mandarin(eng):
    nums = {"0":"ling", "1":"yi", "2":"er",
            "3":"san", "4":"si","5":"wu",
            "6":"liu", "7":"qi", "8":"ba",
            "9":"jiu", "10":"shi"}
    if len(eng) == 1:
        mandarin = nums[eng]
    else:
        if eng.endswith("0"):
            mandarin = nums[eng[0]] + " " + nums["10"]
        else:
            mandarin = nums[eng[0]] + " " + nums["10"] + " " + nums[eng[1]]
    return mandarin

print(convert_to_mandarin("36"))
print(convert_to_mandarin("20"))
print(convert_to_mandarin("16"))