isbncode = "0789751984"

s = int(isbncode[0]) * 1 + int(isbncode[1]) * 2 + int(isbncode[2]) * 3 + int(isbncode[3]) * 4 + int(isbncode[4]) * 5 + int(isbncode[5]) * 6 + int(isbncode[6]) * 7 + int(isbncode[7]) * 8 + int(isbncode[8]) * 9
print(s)

n = 1
d = 0
isbn = isbncode[0:9]
for i in isbn:
    d += int(i) * n
    n = n + 1
print(d)
