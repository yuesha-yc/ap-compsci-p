# Dictionary Exercise 5, p124
institutions = {}
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        line = line.split()
        address = line[1]
        pos = address.find("@")
        domain = address[pos+1:]
        if domain not in institutions:
            institutions[domain] = 1
        else:
            qty = institutions[domain]
            institutions[domain] = qty + 1
print(institutions)
