def multiply(grow, shrink):
    product = 0
    while shrink > 0:
        if shrink%2 == 1:
            product = product + grow
        grow = grow*2
        shrink = shrink // 2
    return product

result = multiply(23,58)
print(result)
range(1,6)